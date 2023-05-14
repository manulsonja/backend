from django.contrib import admin
from .models import *
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
    
class PhotoAdmin(admin.StackedInline):
    model = HutGallery

class MountainHutAdmin(admin.ModelAdmin):
    model = MountainHut
    inlines = [PhotoAdmin]
    formfield_overrides = {
        geomodels.PointField: {'widget': LatLongWidget},
    }
    fields = (
        ('name','rating'),
        'subtitle',
        'image',
        ('telephone', 'email', "website",),
        ('position', 'altitude','hut_type','overnight',),
        ('region', 'gebirge'),
        ('season', 'offseason'),
        'text',
        'author',
    )


admin.site.register(MountainHut, MountainHutAdmin)
