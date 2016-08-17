import math
from django.shortcuts import get_list_or_404, render
from django.http import JsonResponse
from .models import *

def vehicle_types_root(request):
  per_page = int(request.GET.get('per_page', '5'))
  current_page = int(request.GET.get('page', '1'))

  start = (current_page - 1) * per_page

  result = VehicleType.objects.order_by('name')

  total = result.count()
  result_page = result[start:start+5]

  objects = {
    "total": total,
    "pages": math.ceil(total / per_page),
    "current_page": current_page,
    "_embedded": [obj.to_json_hal() for obj in result_page],
    "_links": {
      "self": { "href": "/api/vehicle-types" }
    }
  }
  return JsonResponse(objects, safe=False)
