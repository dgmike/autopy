from django.conf.urls import url
from django.views.generic import TemplateView
from api.views import *

urlpatterns = [
  url(r'^vehicle-types/?$', vehicle_types_root)
]
