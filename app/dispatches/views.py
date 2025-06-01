from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, FormView
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

from .models import Requisition, Movement
from .forms import RequisitionApprovalForm

class PendingRequisitionListView(LoginRequiredMixin, ListView):
    model = Requisition
    template_name = 'pending_list.html'
    context_object_name = 'pending_requisitions'

    def get_queryset(self):
        return Requisition.objects.filter(approvals__isnull=True)


class RequisitionApprovalView(LoginRequiredMixin, FormView):
    template_name = 'approve_requisition.html'
    form_class = RequisitionApprovalForm
    success_url = reverse_lazy('dispatches:movement_list')

    def dispatch(self, request, *args, **kwargs):
        self.requisition = get_object_or_404(Requisition, pk=kwargs['pk'])
        if hasattr(self.requisition, 'approvals'):
            messages.warning(request, 'Requisição já aprovada!')
            return redirect('dispatches:pending_list')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        approval = form.save(commit=False)
        approval.requisition = self.requisition
        approval.approved_by = self.request.user
        approval.save()

        # Criar movimento de estoque
        Movement.objects.create(
            requisition=self.requisition,
            moved_by=self.request.user,
            description='Movimentação gerada após aprovação.'
        )

        messages.success(self.request, 'Requisição aprovada e movimentação registrada!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['requisition'] = self.requisition
        return context

class MovimentListView(LoginRequiredMixin, ListView):
    model = Movement
    template_name = 'movement_list.html'
    context_object_name = 'movements'
