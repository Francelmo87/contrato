import pytest
from django.db import IntegrityError

from app.suppliers.models import Supplier
from app.suppliers.tests.factories import SupplierFactory


# salva corretamente no banco
@pytest.mark.django_db
def test_supplier_is_saved_in_database():
    SupplierFactory()

    assert Supplier.objects.count() == 1
    assert Supplier.pk is not None
    

# Campos persistem corretamente
@pytest.mark.django_db
def test_supplier_fields_are_persisted():
    supplier = SupplierFactory(
        name="fulano",
        cnpj='11111111111111111',
        representative="Cicrano",
        phone='0000000000',
        rg='2222222222',
        cpf='333333333',
    )

    supplier.refresh_from_db()

    assert supplier.name == 'fulano'
    assert supplier.cnpj == '11111111111111111'
    assert supplier.representative == "Cicrano"
    assert supplier.phone == '0000000000'
    assert supplier.rg == '2222222222'
    assert supplier.cpf == '333333333'


# campo opcional aceitam NULL
@pytest.mark.django_db
def test_Supplier_can_be_saved_without_value():
    supplier = SupplierFactory(
        representative=None,
        phone=None,
        rg=None,
        cpf=None,
    )

    assert supplier.representative is None
    assert supplier.phone is None
    assert supplier.rg is None
    assert supplier.cpf is None
    
# Campo obrigatório (name, cnpj)
@pytest.mark.django_db
def test_supplier_fields_is_required():
   
    with pytest.raises(IntegrityError):
          SupplierFactory(
            name=None,
            cnpj=None                
        )


# se o __str__ está correto
@pytest.mark.django_db
def test_supplier_str_representation():
    supplier = SupplierFactory(name="Fornecedor XPTO")

    assert str(supplier) == "Fornecedor XPTO"


# Se está gravando em ordem por nome
@pytest.mark.django_db
def test_supplier_ordering_by_name():
    SupplierFactory(name="Zeta Ltda")
    SupplierFactory(name="Alpha Ltda")

    suppliers = Supplier.objects.all()

    assert suppliers[0].name == "Alpha Ltda"
    