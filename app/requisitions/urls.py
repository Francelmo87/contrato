from django.urls import path

from . import views as v

app_name = 'requisitions'

urlpatterns = [
    path('list/', v.RequisitionListView.as_view(), name='requisition_list'),
    path('create/', v.RequisitionCreateView.as_view(), name='requisition_create'),
]
