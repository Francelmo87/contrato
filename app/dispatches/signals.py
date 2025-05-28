# app.dispatches.signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Movement
from app.contracts.models import ItemContract
from app.requisitions.models import ItemRequesition

@receiver(post_save, sender=Movement)
def update_contract_quantity(sender, instance, created, **kwargs):
    if created:
        requisition = instance.requisition
        for item in requisition.itens_requisition.all():
            contract_item = item.contract_item
            contract_item.quantity -= item.quantity
            contract_item.save()
