from django.shortcuts import render
from django.views.generic import ListView

from . models import Contract

class ContractListView(ListView):
    model= Contract
    template_name = 'contract_list.html'
    context_object_name = 'contracts'
