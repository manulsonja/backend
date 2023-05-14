from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
from pictures.models import PictureField
from multiselectfield import MultiSelectField

def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)


class Zone(models.Model):
    country_choices = [('deutschland','DEUTSCHLAND'), ('oesterreich','OESTERREICH'), ('schweiz','SCHWEIZ'), ('italien','ITALIEN')]
    country = models.CharField( max_length=20, choices=country_choices, null=True)
    name = models.CharField(max_length=50, null=True)
    image = PictureField("Image", upload_to=upload_to, default='tour/default.jpg',  aspect_ratios=["16/9"]) 
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name
    
class Region(models.Model):
    name = models.CharField(max_length=50, null=True)
    image = PictureField("Image", upload_to=upload_to, default='tour/default.jpg',  aspect_ratios=["16/9"]) 
    parent = models.ForeignKey(Zone,on_delete=models.CASCADE,related_name="regions", null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name
    
class Gebirge(models.Model):
    name = models.CharField(max_length=50, null=True)
    image = PictureField("Image", upload_to=upload_to, default='tour/default.jpg',  aspect_ratios=["16/9"]) 
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name