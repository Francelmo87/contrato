from django import forms
from .models import RequisitionApproval

class RequisitionApprovalForm(forms.ModelForm):
    class Meta:
        model = RequisitionApproval
        fields = ['status', 'comments']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'}),
            'comments': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        label={
            'status': 'Situação',
            'comments':'Comentários'
        }
