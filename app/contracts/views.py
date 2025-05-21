from django.shortcuts import render
from django.views.generic import ListView

from . models import Contract

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
