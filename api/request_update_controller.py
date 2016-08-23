import json
from django.shortcuts import get_object_or_404
from django.http import QueryDict
from django.http import JsonResponse
from django.http import HttpResponse

class RequestUpdateController():
  """module to update resource"""
  def put(self, request, pk):
    resource = get_object_or_404(self.queryset, pk=pk)
    data = json.loads(request.body.decode('utf-8'))
    form = self._form(data, instance = resource)
    if not form.is_valid():
      return JsonResponse({'errors': form.errors}, status = 403)
    saved_resource = form.save()
    return JsonResponse(saved_resource.to_json_hal())

  def _form(self, *args, **kawrgs):
    return self.form(*args, **kawrgs)
