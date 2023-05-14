from django.contrib.gis.db import models
from pictures.models import PictureField
from django.utils.text import slugify
from django.utils import timezone
from tinymce import models as tinymce_models

def upload_to(instance, filename):
    return 'huts/{filename}'.format(filename=filename)

parkingtype = (
    ('parkplatz', 'Parkplatz'),
    ('haltestelle', 'Haltestelle'),
    ('stellplatz', 'Stellplatz'),
    ('sonstige', 'Sonstige'),  )

estate_choices = (
    ('public', 'Oeffentlich'),
    ('private', 'Privat'),
)

ground_type_choices = (
    ('asphalt', 'Asphalt'),
    ('schotter', 'Schotter'),
    ('gras', 'Gras'),
    ('erde', 'Erde'),
)

toilet_choices = (
    (True, 'Ja'),
    (False, 'Nein'),  )

class Parking(models.Model): 
  
    text = tinymce_models.HTMLField(null=True)
    short_text = models.CharField(null=True, blank=True)
    image = PictureField(aspect_ratios=["16/9"])
    toilet = models.BooleanField(null=True, choices=toilet_choices)
    fees = models.FloatField(null=True)
    name = models.CharField(max_length=30)   
    capacity = models.IntegerField(null=True)
    position = models.PointField(null=True)
    created = models.DateTimeField(default=timezone.now)
   
    estate = models.CharField(max_length=20, choices=estate_choices, null=True)
    ground_type = models.CharField(max_length=20, choices=ground_type_choices, null=True)
    parkingtype = models.CharField(max_length=20, choices=parkingtype, default='parkplatz')
    slug = models.SlugField(max_length=250, unique_for_date='created', editable=False, null=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    

class ParkingGallery(models.Model):
    image = PictureField("Image", upload_to=upload_to, default='tour/default.jpg',  aspect_ratios=["16/9"]) 
    parent = models.ForeignKey(Parking, on_delete=models.CASCADE, related_name="gallery")
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

