from django.views.generic import ListView


from .models import Requisition


class RequisitionListView(ListView):
    model = Requisition
    template_name = 'requisition_list.html'
    context_object_name = 'requisitions'

