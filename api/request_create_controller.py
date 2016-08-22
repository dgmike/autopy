from django.http import JsonResponse
from django.http.request import QueryDict
from django.core.paginator import Paginator, EmptyPage

class RequestCreateController():
  """Module to create a resource"""
  def post(self, request):
    form = self._form(request.POST)
    if not form.is_valid():
      return JsonResponse({"errors":form.errors}, status=403)

    saved = form.save()

    response = JsonResponse(saved.to_json_hal(), status = 201)
    response['Location'] = saved.self_url()

    return response

  def _model(self):
    return self.model

  def _form(self, request):
    return self.form(request)
