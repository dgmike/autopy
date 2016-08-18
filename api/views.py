import math
from django.views import View
from .models import *
from .request_list_controller import RequestListController

class VehicleTypeRootController(View, RequestListController):
  queryset = VehicleType.objects.order_by('name')
  resource_type = "vehicle_types"

  def _links(self):
    return {
      "self": { "href": "/api/vehicle-types" }
    }
