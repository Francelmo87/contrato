from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from . models import Contract
from . forms import ContractForm

class ContractListView(ListView):
    model= Contract
    template_name = 'contract_list.html'
    context_object_name = 'contracts'

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset


class ContractDetailView(DetailView):
    model = Contract
    template_name = 'contract_detail.html'


class ContractCreateView(CreateView):
    model = Contract
    template_name = 'contract_create.html'
    form_class = ContractForm
    success_url = reverse_lazy('contract_list')