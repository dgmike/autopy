import math
from django.shortcuts import get_list_or_404, render
from django.http import JsonResponse
from django.views import View
from .models import *
from .request_list import RequestList

class VehicleTypeRootController(View, RequestList):
  def get(self, request):
    per_page = self.per_page(request.GET)
    current_page = self.current_page(request.GET)
    start = (current_page - 1) * per_page

    result = VehicleType.objects.order_by('name')

    total = result.count()
    result_page = result[start:start+per_page]

    objects = {
      "total": total,
      "pages": math.ceil(total / per_page),
      "current_page": current_page,
      "_embedded": [obj.to_json_hal() for obj in result_page],
      "_links": {
        "self": { "href": "/api/vehicle-types" }
      }
    }

    return JsonResponse(objects)
