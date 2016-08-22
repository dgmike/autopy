from django.shortcuts import render
from django.views.generic import TemplateView
from django.middleware.csrf import get_token

class HomeView(TemplateView):
  template_name='index.html'

  def get(self, request):
    get_token(request)
    return super(HomeView, self).get(request)
