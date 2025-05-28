from django.urls import path
from . import views as v

app_name = 'dispatches'

urlpatterns = [
    path('pending/', v.PendingRequisitionListView.as_view(), name='pending_list'),
    path('<int:pk>/approve/', v.RequisitionApprovalView.as_view(), name='approve_requisition'),

    path('movement_list/', v.MovimentListView.as_view(), name='moviment_list'),
]