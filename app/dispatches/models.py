
from django.contrib.auth.models import User
from django.db import models

from app.requisitions.models import ItemRequest

# Saída de item aprovada
class ItemDispatch(models.Model):
    request = models.OneToOneField(ItemRequest, on_delete=models.CASCADE)
    dispatched_by = models.ForeignKey(User, on_delete=models.PROTECT)
    dispatch_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Saída para {self.request.item.description}"