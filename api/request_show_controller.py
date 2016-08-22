from django.shortcuts import get_object_or_404
from django.http import JsonResponse

class RequestShowController():
  """module to show resource"""
  def get(self, request, pk):
    resource = get_object_or_404(self.queryset, pk=pk)
    return JsonResponse(resource.to_json_hal())
