import math
from django.views import View
from .models import *
from .forms import *
from .abstract_views import *

class VehicleTypeRootController(View, AbstractListView, AbstractCreateView):
  model = VehicleType
  form = VehicleTypeForm
  queryset = VehicleType.objects.filter(deleted_at__isnull=True).order_by('name')
  resource_type = "vehicle_types"
  permited_filters = ["id__exact", "name__icontains"]

  def _links(self):
    return {
      "self": { "href": "/api/vehicle-types" }
    }

class VehicleTypeItemController(View, AbstractShowView, AbstractUpdateView, AbstractRemoveView):
  queryset = VehicleType.objects.filter(deleted_at__isnull=True)
  form = VehicleTypeForm

class ManufacturerRootController(View, AbstractListView, AbstractCreateView):
  model = Manufacturer
  form = ManufacturerForm
  queryset = Manufacturer.objects.filter(deleted_at__isnull=True).order_by('name')
  resource_type = "manufacturers"
  permited_filters = ["id__exact", "name__icontains", "vehicle_type__id__exact"]

  def _links(self):
    return {
      "self": { "href": "/api/manufacturers" }
    }

class ManufacturerItemController(View, AbstractShowView, AbstractUpdateView, AbstractRemoveView):
  queryset = Manufacturer.objects.filter(deleted_at__isnull=True)
  form = ManufacturerForm
