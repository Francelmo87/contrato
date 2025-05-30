from django import forms

from .models import Contract, ItemContract


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['bidding', 
                  'supplier', 
                  'manager', 
                  'manager_substitute', 
                  'inspector', 
                  'inspector_substitute', 
                  'number', 
                  'target', 
                  'assignature_data', 
                  'start_date', 
                  'end_date', 
                  'value',
                ]
        widgets = {
            'bidding': forms.Select(attrs={'class': 'form-control'}),
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'manager': forms.Select(attrs={'class': 'form-control'}),
            'manager_substitute': forms.Select(attrs={'class': 'form-control'}),
            'inspector': forms.Select(attrs={'class': 'form-control'}),
            'inspector_substitute': forms.Select(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'target': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'assignature_data': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type':'date'}),
            'start_date': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type':'date'}),
            'end_date': forms.DateInput(format='%Y-%m-%d', attrs={'class': 'form-control', 'type':'date'}),
            'value': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'bidding': 'Licitação',
            'supplier': 'Fornecedor',
            'manager': 'Gestor',
            'manager_substitute': 'Gestor Substituto',
            'inspector': 'Fiscal',
            'inspector_substitute': 'Fiscal Substituto',
            'number': 'Número',
            'target': 'Objeto',
            'assignature_data': 'Data da Assinatura',
            'start_date': 'Data Inicial',
            'end_date': 'Data Final',
            'value': 'Valor Total',
        }


class ItemContractForm(forms.ModelForm):
    class Meta:
        model = ItemContract
        fields = ['especification', 'unit', 'quantity', 'unit_price']
        widgets = {
            'especification': forms.Textarea(attrs={'class': 'form-control'}),
            'unit': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'especification': 'Especificação',
            'unit': 'Unidade',
            'quantity': 'Quantidade',
            'unit_price': 'Preço Unitário',
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity <= 0:
            raise forms.ValidationError("Quantidade deve ser maior que zero")
        return quantity
    
    def clean_unit_price(self):
        unit_price = self.cleaned_data.get('unit_price')
        if unit_price <= 0:
            raise forms.ValidationError("Quantidade deve ser maior que zero")
        return unit_price
        
       
class BaseItemContractFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()
        for form in self.forms:
            if not form.has_changed() and self.can_delete:
                continue
            if not form.is_valid():
                continue


ItemContractFormSet = forms.inlineformset_factory(
    Contract,
    ItemContract,
    form = ItemContractForm,
    formset = BaseItemContractFormSet,
    extra = 1,  # Pode ajustar conforme desejar
    can_delete=False,
)
