from xml.dom import HierarchyRequestErr
from django.contrib import admin
from .models import *

class PhotoAdmin(admin.StackedInline):
    model = Image

class WandernAdmin(admin.ModelAdmin):
    model = Wandern
    exclude=('track',)
    readonly_fields=('distance','geojson_track','elevation_gain',)
    inlines = [PhotoAdmin]

class SkitourAdmin(admin.ModelAdmin):
    model = Skitour
    exclude=('track',)
    readonly_fields=('distance','geojson_track','elevation_gain',)
    inlines = [PhotoAdmin]
class HikeAndFlyAdmin(admin.ModelAdmin):
    model = HikeAndFly
    exclude=('track',)
    readonly_fields=('distance','geojson_track','elevation_gain',)
    inlines = [PhotoAdmin]
class KlettertourAdmin(admin.ModelAdmin):
    model = Klettertour
    exclude=('track',)
    readonly_fields=('distance','geojson_track','elevation_gain',)
    inlines = [PhotoAdmin]
class HochtourAdmin(admin.ModelAdmin):
    model = Hochtour
    exclude=('track',)
    readonly_fields=('distance','geojson_track','elevation_gain',)
    inlines = [PhotoAdmin]
    fields = (
        ('title','rating',),
        ('subtitle','tour_duration'),
        'gpxfile',
        'image',
        ('fitness_difficulty','tech_difficulty', 'region'),
        ('season', 'offseason'),
        'text',
        'author',
    )
admin.site.register(Klettertour, KlettertourAdmin)
admin.site.register(Skitour,SkitourAdmin)
admin.site.register(Wandern, WandernAdmin)
admin.site.register(HikeAndFly, HikeAndFlyAdmin)
admin.site.register(Hochtour, HochtourAdmin)
admin.site.register(Image)




