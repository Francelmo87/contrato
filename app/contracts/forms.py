
from django import forms
from .models import Contract


class ContractForm(forms.ModelForm):

    class Meta:
        model = Contract
        fields = ['bidding', 'supplier', 'number', 'target', 'assignature_data', 'start_date', 'end_date','expire','formatted_value']
        widgets = {
            'bidding': forms.Select(attrs={'class': 'form-control'}),
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'target': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'assignature_data': forms.DateInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control'}),
            'expire': forms.DateInput(attrs={'class': 'form-control'}),
            'formatted_value': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'bidding': 'Licitação',
            'supplier': 'Fornecedor',
            'number': 'Número',
            'target': 'Objeto',
            'assignature_data': 'Data da Assinatura',
            'start_date': 'Data Inicial',
            'end_date': 'Data Final',
            'expire': 'Vigência',
            'formatted_value': 'Valor Total',
        }
