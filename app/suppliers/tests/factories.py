import factory
from app.suppliers.models import Supplier


class SupplierFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Supplier

    name = factory.Faker("company")
    phone = factory.Faker("phone_number")

    cnpj = factory.Faker("numerify", text="##############")
    representative = factory.Faker("name")
    rg = factory.Faker("numerify", text="#########")
    cpf = factory.Faker("numerify", text="###########")
