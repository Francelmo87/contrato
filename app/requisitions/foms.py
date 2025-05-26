from django import forms

from .models import Requisition, ItemRequesition


class RequisitionForm(forms.ModelForm):
    class Meta:
        model = Requisition
        fields = ['contract', 'requested_by', ]
        exclude = ['approved']
        widgets = {
            'contract': forms.Select(attrs={'class': 'form-control'}),
            'requested_by': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'contract': 'Contrato',
            'requested_by': 'Responsável',
        }
       

class ItemRequisitionForm(forms.ModelForm):
    class Meta:
        model = ItemRequesition
        fields = ['contract_item', 'quantity']
        widgets = {
            'contract_item': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'contract_item': 'Item',
            'quantity': 'Quantidade',
        }

        def clean_quantity(self):
            quantity = self.cleaned_data.get('quantity')
            if quantity <= 0:
                raise forms.ValidationError("Quantidade deve ser maior que zero")
            return quantity

       

class BaseItemRequisitionFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()
        for form in self.forms:
            if not form.has_changed() and self.can_delete:
                continue
            if not form.is_valid():
                continue


ItemRequisitionFormSet = forms.inlineformset_factory(
    Requisition,
    ItemRequesition,
    form = ItemRequisitionForm,
    formset = BaseItemRequisitionFormSet,
    extra = 1,  # Pode ajustar conforme desejar
    can_delete=False,
)