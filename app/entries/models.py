from django.contrib.auth.models import User
from django.db import models

from app.contracts.models import ContractItem


# Entradas de itens no contrato
class ContractEntry(models.Model):
    item = models.ForeignKey(ContractItem, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    entry_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Entrada de {self.quantity} - {self.item}"
