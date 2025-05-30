from django.db import models
from datetime import date
from django.contrib.auth.models import User

from app.base.models import TimeStampedModel

from app.biddings.models import Bidding
from app.suppliers.models import Supplier


# Contrato
class Contract(TimeStampedModel):
    bidding = models.ForeignKey(Bidding, on_delete=models.SET_NULL, null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    
    manager = models.ForeignKey(User, on_delete=models.PROTECT, related_name='manager_contracts')
    manager_substitute = models.ForeignKey(User, on_delete=models.PROTECT, related_name='manager_sustitute_contracts')
    inspector = models.ForeignKey(User, on_delete=models.PROTECT, related_name='inspector_contracts')
    inspector_substitute = models.ForeignKey(User, on_delete=models.PROTECT, related_name='inspector_substitute_contracts')

    number = models.CharField('Número', max_length=20)
    target = models.TextField('Objeto')
    assignature_data = models.DateField('Data da assinatura')
    start_date = models.DateField('Data inicial')
    end_date = models.DateField('Data final')
    value = models.DecimalField('Valor total', max_digits=15, decimal_places=2 , default=0)

    class Meta:
        ordering = ('number',)
        verbose_name_plural = 'Contratos'

    def __str__(self):
        return f"Contrato {self.number} - {self.supplier.name}"

    @property
    def formatted_value(self):
        return f"R$ {self.value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    @property
    def expire(self):
        today = date.today()
        days_remainning = (self.end_date - today).days
        return days_remainning
    

    def get_queryset(self):
        user = self.request.user
        
        # Se admin (superuser ou grupo 'Administradores') vê tudo
        if user.is_superuser or user.groups.filter(name='Administrator').exists():
            return Contract.objects.all()

        # Se gestor ou suplente de gestor
        if user.groups.filter(name__in=['manager', 'manager_substitute']).exists():
            return Contract.objects.filter(models.Q(manager=user) | models.Q(manager_substitute=user))

        # Se fiscal ou suplente de fiscal
        if user.groups.filter(name__in=['inspector', 'inspector_substitute']).exists():
            return Contract.objects.filter(models.Q(inspector=user) | models.Q(inspector_substitute=user))

        # Outros → não vê nada
        return Contract.objects.none()

# Itens do contrato
class ItemContract(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, related_name='items')
    especification = models.TextField('Especificação',)
    unit = models.CharField('Unidade',max_length=20)
    quantity = models.PositiveIntegerField('Quantidade')
    unit_price = models.DecimalField('Preço unitário', max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.especification} ({self.contract.number})"
    
    @property
    def formatted_unit_price(self):
        return f"R$ {self.unit_price:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    @property
    def total_value(self):
        value = self.quantity * self.unit_price
        return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
   
    
# Adito do Contrato
class Amendment(TimeStampedModel):
    contract = models.ForeignKey(Contract, related_name='amendments', on_delete=models.CASCADE)
    type = models.CharField('Tipo', max_length=20, choices=[('prorrogacao', 'Prorrogação'), ('financeiro', 'Financeiro'), ('misto', 'Misto')])
    motivation = models.TextField('Motivação')
    new_end_date = models.DateField('Nova data final',blank=True, null=True)
    new_value = models.DecimalField('Valor novo', max_digits=15, decimal_places=2, default=0)

#Aditivo dos itens do contrato
class ItemAmendment(models.Model):
    aditivo = models.ForeignKey(Amendment, related_name='itens_new', on_delete=models.CASCADE)
    especification = models.TextField('Especificação')
    quantity = models.PositiveIntegerField('Quantidade')
    unit = models.CharField('Unidade',max_length=20)
    unit_price = models.DecimalField(max_digits=12, decimal_places=2)
