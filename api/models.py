from django.db import models

class VehicleType(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name

  def to_json_hal(self):
    return {
      "id": self.id,
      "name": self.name,
      "_links": {
        "self": ("/api/vehicle-types/%s" % self.id)
      }
    }
