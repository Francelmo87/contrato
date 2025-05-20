from django.db import models

from app.base.models import TimeStampedModel

# Fornecedor
class Supplier(TimeStampedModel):
    name = models.CharField('empresa', max_length = 200, null=True, blank=True)
    cnpj = models.CharField('cnpj', max_length = 17, null=True, blank=True)
    representative = models.CharField('representante', max_length = 200, null=True, blank=True)
    phone = models.CharField('contato', max_length = 15,)
    rg = models.CharField('rg', max_length = 13, null=True, blank=True)
    cpf = models.CharField('cpf', max_length = 11, null=True, blank=True)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name