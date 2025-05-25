from django.contrib.auth.models import User
from django.db import models

from app.contracts.models import ItemContract

# Solicitação de item
class ItemRequest(models.Model):
    item = models.ForeignKey(ItemContract, on_delete=models.CASCADE)
    requested_quantity = models.PositiveIntegerField()
    requested_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='requests')
    request_date = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True, related_name='approvals')
    approval_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Solicitação {self.id} - {self.item.description}"