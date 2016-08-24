from django.conf.urls import url
from django.views.generic import TemplateView
from api.views import *

urlpatterns = [
  url(r'^vehicle-types/?$', VehicleTypeRootController.as_view()),
  url(r'^vehicle-types/(?P<pk>[0-9]+)/?$', VehicleTypeItemController.as_view()),

  url(r'^manufacturers/?$', ManufacturerRootController.as_view()),
  url(r'^manufacturers/(?P<pk>[0-9]+)/?$', ManufacturerItemController.as_view()),

  url(r'^vehicles/?$', VehicleRootController.as_view()),
  url(r'^vehicles/(?P<pk>[0-9]+)/?$', VehicleItemController.as_view()),
]
