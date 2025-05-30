from django.db import models

from app.base.models import TimeStampedModel

# Licitação
class Bidding(TimeStampedModel):
    number = models.CharField('numero', max_length=50)
    modality = models.CharField('modalidade', max_length=100)
    year = models.PositiveIntegerField('ano')
    approval_date = models.DateField('data da Homologação')
    value = models.DecimalField('valor', max_digits=11, decimal_places=2, null=True, blank=True)

    class Meta:
        ordering = ['number']
        verbose_name_plural = 'Licitações'
    
    def __str__(self):
        return f"{self.number}/{self.year}"