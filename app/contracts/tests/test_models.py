
import pytest
from datetime import date, timedelta
from decimal import Decimal
from django.db import IntegrityError


from django.contrib.auth import get_user_model
from app.contracts.models import Contract
from app.contracts.models import ItemContract
from app.biddings.tests.factories import BiddingFactory
from app.contracts.tests.factories import ContractFactory, ItemContractFactory
from app.suppliers.tests.factories import SupplierFactory


# testa a criação com os relacionamentos(integridadde referencial)
@pytest.mark.django_db
def test_contract_is_created_with_relationships():
    contract = ContractFactory()

    assert contract.pk is not None
    assert contract.supplier is not None
    assert contract.bidding is not None
    
    
# testa o funcionamento dos on_delete = CASCADE (Supplier)
@pytest.mark.django_db
def test_contract_is_deleted_when_supplier_is_deleted():
    contract = ContractFactory()
    supplier = contract.supplier

    supplier.delete()

    assert Contract.objects.count() == 0


# testa o funcionamento dos on_delete = SET_NULL (Bidding)
@pytest.mark.django_db
def test_contract_bidding_is_set_null_when_bidding_is_deleted():
    contract = ContractFactory()
    bidding = contract.bidding

    bidding.delete()
    contract.refresh_from_db()

    assert contract.bidding is None


# testa o funcionamento dos on_delete = CASCADE (Supplier)
@pytest.mark.django_db
def test_supplier_reverse_relationship():
    supplier = SupplierFactory()
    ContractFactory(supplier=supplier)
    ContractFactory(supplier=supplier)

    assert supplier.suppliers.count() == 2


# testa o relacionamento reverso 
@pytest.mark.django_db
def test_supplier_reverse_relationship():
    supplier = SupplierFactory()
    ContractFactory(supplier=supplier)
    ContractFactory(supplier=supplier)

    assert supplier.suppliers.count() == 2


# testa os campos obrigratorio
@pytest.mark.django_db
def test_contract_number_is_required():
    with pytest.raises(IntegrityError):
        ContractFactory(number=None)


# testa o __str__
@pytest.mark.django_db
def test_contract_str_representation():
    contract = ContractFactory(number="123")

    assert str(contract) == f"Contrato 123 - {contract.supplier.name}"
    

# testa o formato do valor no padrão brasileiro (Property)   
@pytest.mark.django_db
def test_contract_formatted_value():
    contract = ContractFactory(value=1234.56)

    assert contract.formatted_value == "R$ 1.234,56"
    

from datetime import date, timedelta


# testa se o contrato esta expirando na data correta
@pytest.mark.django_db
def test_contract_expire_days():
    end_date = date.today() + timedelta(days=10)
    contract = ContractFactory(end_date=end_date)

    assert contract.expire == 10

# -------------------------------------------------------------------------------------

# testa se item do contrato está criando corretamente
@pytest.mark.django_db
def test_item_contract_is_created():
    item = ItemContractFactory()

    assert item.pk is not None
    assert item.contract is not None
    

# testa se on_delete = CASCADE deleta os itens em cascata
@pytest.mark.django_db
def test_items_are_deleted_when_contract_is_deleted():
    contract = ContractFactory()
    ItemContractFactory(contract=contract)
    ItemContractFactory(contract=contract)

    contract.delete()

    assert ItemContract.objects.count() == 0
    

# testa se o relacionamento reverso funciona
@pytest.mark.django_db
def test_contract_items_reverse_relationship():
    contract = ContractFactory()
    ItemContractFactory(contract=contract)
    ItemContractFactory(contract=contract)

    assert contract.items.count() == 2


# testa se os itens obrigatórios do contrato estão certos 
@pytest.mark.django_db
def test_item_contract_contract_is_required():
    with pytest.raises(IntegrityError):
        ItemContractFactory(contract=None)
        
        
# testa o __str__ está correto
@pytest.mark.django_db
def test_item_contract_str_representation():
    item = ItemContractFactory(especification="Item Teste")

    assert str(item) == f"Item Teste ({item.contract.number})"
    

# testa o formato de valor unitario
@pytest.mark.django_db
def test_item_contract_formatted_unit_price():
    item = ItemContractFactory(unit_price=Decimal("1234.50"))

    assert item.formatted_unit_price == "R$ 1.234,50"


# testa o valor total se ta fazendo o cálculo correto
@pytest.mark.django_db
def test_item_contract_total_value():
    item = ItemContractFactory(
        quantity=10,
        unit_price=Decimal("20.00")
    )

    assert item.total_value == "R$ 200,00"
