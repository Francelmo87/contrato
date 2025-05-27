from django.db import models
from django.contrib.auth.models import User
from app.requisitions.models import Requisition

class RequisitionApproval(models.Model):
    requisition = models.OneToOneField(Requisition, on_delete=models.CASCADE, related_name='approvals')
    approved_by = models.ForeignKey(User, on_delete=models.PROTECT)
    approved_at = models.DateTimeField('Aprovado em',auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('approved', 'Aprovado'), ('rejected', 'Rejeitado')],
        default='approved'
    )
    comments = models.TextField('Comentários',blank=True, null=True)

    def __str__(self):
        return f"Aprovação de {self.requisition} - {self.status}"


class Movement(models.Model):
    requisition = models.ForeignKey(Requisition, on_delete=models.CASCADE, related_name='movements')
    moved_by = models.ForeignKey(User, on_delete=models.PROTECT)
    moved_at = models.DateTimeField('Movido em',auto_now_add=True)
    description = models.TextField('Descrição')

    def __str__(self):
        return f"Movimento: {self.requisition} por {self.moved_by}"
