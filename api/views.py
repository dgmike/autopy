import math
from django.shortcuts import get_list_or_404, render
from django.http import JsonResponse
from django.views import View
from .models import *
from .request_list_controller import RequestListController

class VehicleTypeRootController(View, RequestListController):
  queryset = VehicleType.objects.order_by('name')

  def _filter(self, queryset, querydict):
    # TODO: add filters
    return queryset

  def get(self, request):
    per_page, current_page, start = self._pagination_args(request.GET)
    result = self._filter(self.queryset, request.GET)

    total = result.count()
    result_page = result[start:start+per_page]

    objects = {
      "total": total,
      "pages": math.ceil(total / per_page),
      "per_page": per_page,
      "current_page": current_page,
      "_embedded": {
        "vehicle_types": [obj.to_json_hal() for obj in result_page]
      },
      "_links": {
        "self": { "href": "/api/vehicle-types" }
      }
    }

    return JsonResponse(objects)
