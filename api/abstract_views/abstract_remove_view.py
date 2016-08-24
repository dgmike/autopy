from django.shortcuts import get_object_or_404
from django.http import HttpResponse

class AbstractRemoveView():
  """module to remove resource"""
  def delete(self, request, pk):
    resource = get_object_or_404(self.queryset, pk=pk)
    resource.delete()
    return HttpResponse('', status = 200)
