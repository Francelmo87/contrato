from django.urls import path

from  . import views as v

app_name='contracts'

urlpatterns = [
    path('list/', v.ContractListView.as_view(), name='contract_list' ),
    path('<int:pk>/detail/', v.ContractDetailView.as_view(), name='contract_detail' ),
]