from django.db import models

from app.base.models import TimeStampedModel

from app.biddings.models import Bidding
from app.suppliers.models import Supplier


# Contrato
class Contract(TimeStampedModel):
    bidding = models.ForeignKey(Bidding, on_delete=models.SET_NULL, null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    number = models.CharField('número',max_length=50)
    target = models.TextField('objeto')
    assignature_data = models.DateField('data da assinatura')
    start_date = models.DateField('data inicial')
    end_date = models.DateField('data final')

    def __str__(self):
        return f"Contrato {self.number} - {self.supplier.name}"

    @property
    def vigencia(self):
        return f"{self.start_date} a {self.end_date}"

# Itens do contrato
class ContractItem(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='items')
    description = models.TextField('especificação',)
    unit = models.CharField('unidade',max_length=20)
    quantity = models.PositiveIntegerField('quantidade')
    unit_price = models.DecimalField('preço unitário',max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.description} ({self.contract.number})"

    @property
    def total_value(self):
        return self.quantity * self.unit_price