import math
from django.shortcuts import get_list_or_404, render
from django.http import JsonResponse
from django.views import View
from .models import *
from .request_list_controller import RequestListController

class VehicleTypeRootController(View, RequestListController):
  queryset = VehicleType.objects.order_by('name')
  resource_type = "vehicle_types"

  def _filter(self, queryset, querydict):
    # TODO: add filters
    return queryset

  def _links(self):
    return {
      "self": { "href": "/api/vehicle-types" }
    }

  def get(self, request):
    per_page, current_page, start = self._pagination_args(request.GET)
    queryset_filtered = self._filter(self.queryset, request.GET)

    total = queryset_filtered.count()
    result_page = queryset_filtered[start:start+per_page]
    pages = math.ceil(total / per_page)
    hal_objects = [obj.to_json_hal() for obj in result_page]

    objects = {
      "total": total,
      "pages": pages,
      "per_page": per_page,
      "current_page": current_page,
      "_embedded": {
        self.resource_type: hal_objects
      },
      "_links": self._links()
    }

    return JsonResponse(objects)
