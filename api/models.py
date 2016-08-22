from django.db import models

class VehicleType(models.Model):
  name = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

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
