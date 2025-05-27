from django.utils import timezone
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from .foms import ItemRequisitionFormSet, RequisitionForm
from .models import Requisition


class RequisitionListView(ListView):
    model = Requisition
    template_name = 'requisition_list.html'
    context_object_name = 'requisitions'


class RequisitionCreateView(CreateView):
    model = Requisition
    form_class = RequisitionForm
    template_name = 'requisition_create.html'
    success_url = reverse_lazy('requisitions:requisition_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = ItemRequisitionFormSet(self.request.POST)
        else:
            context['formset'] = ItemRequisitionFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()  
            return super().form_valid(form)
        return self.render_to_response(self.get_context_data(form=form))


class RequisitionDetailView(DetailView):
    model = Requisition
    template_name = 'requisition_detail.html'
