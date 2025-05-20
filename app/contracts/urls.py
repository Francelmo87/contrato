from django.urls import path

from  .views import ContractListView

app_name='contracts'

urlpatterns = [
    path('list/', ContractListView.as_view(), name='contract_list' ),
]