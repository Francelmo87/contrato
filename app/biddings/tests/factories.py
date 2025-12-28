import datetime
import factory
from decimal import Decimal
from app.biddings.models import Bidding

# Criação da classe modelo do banco de dados de licitação
class BiddingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Bidding

    number = factory.Sequence(lambda n: f"{n:03d}")
    modality = "Pregão"
    year = 2025
    approval_date = datetime.date(2025, 1, 10)
    value = Decimal("10000.00")
