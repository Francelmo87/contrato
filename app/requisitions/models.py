from django.conf import settings
from django.db import models

from app.base.models import TimeStampedModel

from app.contracts.models import Contract, ItemContract


class Requisition(TimeStampedModel):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    requested_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='requisitions')
    
    def __str__(self):
        return self.contract.number    


# Solicitação de item
class ItemRequesition(models.Model):
    requisition = models.ForeignKey(Requisition, on_delete=models.CASCADE, related_name='itens_requisition')
    contract_item = models.ForeignKey(ItemContract, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField('Quantidade')
    

    def __str__(self):
        return f"{self.quantity} x {self.contract_item.especification}"