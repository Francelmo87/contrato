import datetime
import pytest
from django.core.exceptions import ValidationError

from app.biddings.tests.factories import BiddingFactory
from app.biddings.models import Bidding


# salva corretamente no banco
@pytest.mark.django_db
def test_bidding_is_saved_in_datebase():
    BiddingFactory()
    
    assert Bidding.objects.count() == 1 
    

# Campos persistem corretamente
@pytest.mark.django_db
def test_bidding_fields_are_persisted():
    bidding = BiddingFactory(
        number="123",
        modality="Concorrência",
        year=2024
    )

    bidding.refresh_from_db()

    assert bidding.number == "123"
    assert bidding.modality == "Concorrência"
    assert bidding.year == 2024


# campo opcional(value)
@pytest.mark.django_db
def test_bidding_can_be_saved_without_value():
    bidding = BiddingFactory(value=None)

    assert bidding.value is None
    
# Campo obrigatório (number) — VALIDAÇÃO DJANGO
def test_bidding_number_is_required():
    bidding = Bidding(
        modality="Pregão",
        year=2025,
        approval_date=datetime.date.today(),
    )

    with pytest.raises(ValidationError):
        bidding.full_clean()    


# se o __str__ está correto
@pytest.mark.django_db
def test_bidding_str_representation():
    bidding = BiddingFactory(number="045", year=2023)

    assert str(bidding) == "045/2023"

# Se Ordering definido no model
@pytest.mark.django_db
def test_bidding_default_ordering():
    BiddingFactory(number="200")
    BiddingFactory(number="100")

    biddings = Bidding.objects.all()

    assert biddings[0].number == "100"

