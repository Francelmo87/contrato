from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import ContractForm, ItemContractFormSet
from .models import Contract

class ContractListView(LoginRequiredMixin, ListView):
    model= Contract
    template_name = 'contract_list.html'
    context_object_name = 'contracts'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset


class ContractDetailView(LoginRequiredMixin, DetailView):
    model = Contract
    template_name = 'contract_detail.html'


class ContractCreateView(LoginRequiredMixin, CreateView):
    model = Contract
    form_class = ContractForm
    template_name = 'contract_create.html'
    success_url = reverse_lazy('contracts:contract_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = ItemContractFormSet(self.request.POST)
        else:
            context['formset'] = ItemContractFormSet()
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