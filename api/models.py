from django.db import models
import datetime

class AbstractBaseModel(models.Model):
  created_at = models.DateTimeField(auto_now_add=True, db_index=True)
  updated_at = models.DateTimeField(auto_now=True, db_index=True)
  deleted_at = models.DateTimeField(null=True, db_index=True)

  class Meta:
    abstract = True

  def has_some(self, relationship):
    relationship_set = "%s_set" % relationship
    count = getattr(self, relationship_set).filter(deleted_at__isnull=True).count()
    return count > 0

  def delete(self, *args, **kwargs):
    self.deleted_at = datetime.datetime.now()
    self.save()

  def drop(self):
    super(__class__, self).delete()

class VehicleType(AbstractBaseModel):
  name = models.CharField(max_length=100, db_index=True)

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
    return "/api/vehicle-types/%d" % self.id

class Manufacturer(AbstractBaseModel):
  name = models.CharField(max_length=100, db_index=True)
  vehicle_type = models.ForeignKey('VehicleType', on_delete=models.PROTECT, db_index=True)

  def __str__(self):
    return self.name

  def to_json_hal(self):
    return {
      "id": self.id,
      "name": self.name,
      "created_at": self.created_at,
      "updated_at": self.updated_at,
      "_links": {
        "self": self.self_url(),
        "manufacturers_item": self.vehicle_type.self_url()
      },
      "_embedded": {
        "vehicle_type": {
          "id": self.vehicle_type.id,
          "name": self.vehicle_type.name
        }
      }
    }

  def self_url(self):
    return "/api/manufacturer/%d" % self.id

class Vehicle(AbstractBaseModel):
  manufacturer = models.ForeignKey('Manufacturer', on_delete=models.PROTECT, db_index=True)
  model = models.CharField(max_length=100, db_index=True)
  color = models.CharField(max_length=100, db_index=True)
  rotated = models.PositiveIntegerField(db_index=True, blank=True)
  motor = models.CharField(max_length=100, db_index=True)

  def __str__(self):
    return self.model

  def to_json_hal(self):
    return {
      "id": self.id,
      "model": self.model,
      "color": self.color,
      "rotated": self.rotated,
      "motor": self.motor,
      "created_at": self.created_at,
      "updated_at": self.updated_at,
      "_embedded": {
        "manufacturer": {
          "id": self.manufacturer.id,
          "name": self.manufacturer.name
        },
        "vehicle_type": {
          "id": self.manufacturer.vehicle_type.id,
          "name": self.manufacturer.vehicle_type.name
        }
      },
      "_links": {
        "self": self.self_url(),
        "manufacturer": self.manufacturer.self_url(),
        "vehicle_type": self.manufacturer.vehicle_type.self_url(),
      }
    }

  def self_url(self):
    return "/api/vehicles/%d" % self.id
