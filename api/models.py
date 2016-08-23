from django.db import models
import datetime

class VehicleType(models.Model):
  name = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  deleted_at = models.DateTimeField(null=True)

  def __str__(self):
    return self.name

  def to_json_hal(self):
    return {
      "id": self.id,
      "name": self.name,
      "created_at": self.created_at,
      "updated_at": self.updated_at,
      "_links": {
        "self": self.self_url()
      }
    }

  def self_url(self):
    return "/api/vehicle-types/%s" % self.id

  def delete(self, *args, **kwargs):
    self.deleted_at = datetime.datetime.now()
    self.save()