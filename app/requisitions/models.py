from django.contrib.auth.models import User
from django.db import models

from app.base.models import TimeStampedModel

from app.contracts.models import Contract, ItemContract


class Requisition(TimeStampedModel):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    requested_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='requisitions')
    
    approved = models.BooleanField('Aprovado',default=False)
    approved_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT, related_name='approved_requisitions')
    approval_date = models.DateTimeField('Data da aproivação',null=True, blank=True)

    def __str__(self):
        return self.contract.number    


# Solicitação de item
class ItemRequesition(models.Model):
    requisition = models.ForeignKey(Requisition, on_delete=models.CASCADE, related_name='itens_requisition')
    contract_item = models.ForeignKey(ItemContract, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField('Quantidade')
    

    def __str__(self):
        return f"{self.quantity} x {self.contract_item.especification}"