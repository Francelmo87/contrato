from django.db import models

from app.base.models import TimeStampedModel

from app.biddings.models import Bidding
from app.suppliers.models import Supplier


# Contrato
class Contract(TimeStampedModel):
    bidding = models.ForeignKey(Bidding, on_delete=models.SET_NULL, null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    number = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Contrato {self.number} - {self.supplier.name}"


# Itens do contrato
class ContractItem(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='items')
    description = models.TextField()
    unit = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.description} ({self.contract.number})"

    @property
    def total_value(self):
        return self.quantity * self.unit_price