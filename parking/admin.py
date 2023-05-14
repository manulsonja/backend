from django.contrib import admin
from .models import Parking, ParkingGallery
from django.contrib.gis.db import models as geomodels
from django import forms
from django.contrib.gis.geos import Point


class LatLongWidget(forms.MultiWidget):
    """
    A Widget that splits Point input into latitude/longitude text inputs.
    """

    def __init__(self, attrs=None, date_format=None, time_format=None):
        widgets = (forms.TextInput(attrs={"title": "Longitude"}),
                   forms.TextInput(attrs={"title": "Latitude"}))
        super(LatLongWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return tuple(value.coords)
        return (None, None)

    def value_from_datadict(self, data, files, name):
        mylat = data[name + '_0']
        mylong = data[name + '_1']

        try:
            point = Point(float(mylat), float(mylong))
        except ValueError:
            return ''

        return point
    

   
class GalleryAdmin(admin.StackedInline):
    model = ParkingGallery

class ParkingAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'image',
        'position',
        ('parkingtype','capacity'), 
        ('fees', 'estate', 'ground_type','toilet'),
        'short_text',
        'text',
    )
    model = Parking
    inlines = [GalleryAdmin]
    formfield_overrides = {
        geomodels.PointField: {'widget': LatLongWidget},
    }

admin.site.register(Parking, ParkingAdmin)  

