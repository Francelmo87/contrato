from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ItemRequesition


@receiver(post_save, sender=ItemRequesition)
def update_requisition_quantity(sender, instance, created, **kwargs):
    if created:
        if instance.quantity > 0:
            contract = instance.contract_item
            contract.quantity -= instance.quantity
            contract.save()