import math
from django.views import View
from .models import *
from .forms import *
from .request_list_controller import RequestListController
from .request_create_controller import RequestCreateController
from .request_show_controller import RequestShowController
from .request_update_controller import RequestUpdateController
from .request_remove_controller import RequestRemoveController

class VehicleTypeRootController(View, RequestListController, RequestCreateController):
  model = VehicleType
  form = VehicleTypeForm
  queryset = VehicleType.objects.filter(deleted_at__isnull=True).order_by('name')
  resource_type = "vehicle_types"
  permited_filters = ["id__exact", "name__icontains"]

  def _links(self):
    return {
      "self": { "href": "/api/vehicle-types" }
    }

class VehicleTypeItemController(View, RequestShowController, RequestUpdateController, RequestRemoveController):
  queryset = VehicleType.objects.filter(deleted_at__isnull=True)
  form = VehicleTypeForm
