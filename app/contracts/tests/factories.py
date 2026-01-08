import factory
from datetime import date, timedelta
from decimal import Decimal

from django.contrib.auth import get_user_model

from app.contracts.models import Contract, ItemContract
from app.biddings.tests.factories import BiddingFactory
from app.suppliers.tests.factories import SupplierFactory



User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user{n}")


class ContractFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Contract

    bidding = factory.SubFactory(BiddingFactory)
    supplier = factory.SubFactory(SupplierFactory)
    manager = factory.SubFactory(UserFactory)
    inspector = factory.SubFactory(UserFactory)

    number = factory.Sequence(lambda n: f"CT-{n}")
    target = "Prestação de serviços"
    assignature_data = factory.LazyFunction(date.today)
    start_date = factory.LazyFunction(date.today)
    end_date = factory.LazyFunction(lambda: date.today() + timedelta(days=365))
    value = 10000


class ItemContractFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ItemContract

    contract = factory.SubFactory(ContractFactory)
    especification = factory.Faker("sentence")
    unit = "UN"
    quantity = 10
    unit_price = Decimal("15.50")