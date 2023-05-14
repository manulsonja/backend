from email.policy import default
from tinymce import models as tinymce_models
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import NewUser 
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from utils.parser.parse import parse_gpx, naive_elevation
from django.conf import settings
from django.utils.text import slugify
from shapely import wkt
import pyproj
from shapely.ops import transform
from functools import partial
from django.utils.translation import gettext_lazy as _
import shapely
import PIL.Image
from pictures.models import PictureField
from multiselectfield import MultiSelectField
from geography.models import Region
from django.contrib.postgres.fields import ArrayField

diff_choices = [
        ("leicht","LEICHT"),
        ("mittel","MITTEL"),
        ("schwierig","SCHWIERIG"),
       ]
season_multichoices = (
        ('1','January'),
        ('2','February'),('3','March'),('4','April'),
        ('5','Mai'),('6','June'),('7','July'),
        ('8','August'),('9','September'),('10','Octobre'),
        ('11','November'),('12','Decembre'),
    )
options = (
        ('draft', 'Draft'),
        ('published', 'Published'),)
rating_choices = [
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),]
 
def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)
  
class Tour(models.Model):

    tour_duration = models.DurationField(null=True)
    gpxfile = models.FileField(upload_to='files', null=True)
    track = models.LineStringField(null=True, dim=3, srid=4326)
    geojson_track = models.TextField(null=True)
    tourtype = models.CharField(max_length=30, editable=False)
    
    class TourObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')
    
    distance = models.IntegerField(null=True)
    elevation_gain = models.FloatField(null=True)
    elevation_values = ArrayField(models.FloatField(max_length=10, blank=True),blank=True, null=True)
    steps = ArrayField(models.FloatField(max_length=10, blank=True),blank=True, null=True)
    
    region = models.ForeignKey(Region,on_delete=models.CASCADE,related_name="regionen", null=True)
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=100)
    text =  tinymce_models.HTMLField()
    season = MultiSelectField(choices=season_multichoices, max_length=100, default=None)
    offseason = MultiSelectField(choices=season_multichoices, max_length=100, default=None)

    image = PictureField("Image", upload_to=upload_to, default='tour/default.jpg',  aspect_ratios=["16/9"])
    created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        NewUser, on_delete=models.CASCADE, related_name='tour_posts',) 
    status = models.CharField(
        max_length=10, choices=options, default='published')
    rating = models.CharField(
        max_length=1,
        choices=rating_choices,
        default='1',)
    difficulty = models.CharField(
        max_length=10,
        default='schwierig',
        editable=False)

    slug = models.SlugField(max_length=250, unique_for_date='created', editable=False)
    objects = models.Manager()  # default manager
    tourobjects = TourObjects()  # custom manager

    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        file_url = self.gpxfile
        ls = parse_gpx(file_url)
        self.track = ls
        shapely_ls = wkt.loads(ls.wkt)
        self.geojson_track = shapely.to_geojson(shapely_ls)
        self.elevation_gain, self.elevation_values, self.steps =  naive_elevation(ls)
        
        project = partial(
            pyproj.transform,
            pyproj.Proj('EPSG:4326'),
            pyproj.Proj('EPSG:32633'))
        line2 = transform(project, shapely_ls)
        self.distance = int(line2.length)

        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Image(models.Model):
    image = PictureField("Image", upload_to=upload_to, default='tour/default.jpg',  aspect_ratios=["16/9"]) 
    parent = models.ForeignKey(Tour,on_delete=models.CASCADE,related_name="album")
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Klettertour(Tour):
    protection_choices=[(0,"alpin"),(1,"mittel"),(2,"gut"),(3,"sehr gut")]
    grades_choices=[("1",0),("1+",1),
                    ("2-",2),("2",3),("2+",4),
                    ("3-",5),("3",6),("3+",7),
                    ("4-",8),("4",9),("4+",10),
                    ("5-",11),("5",12),("5+",13),
                    ("6-",14),("6",15),("6+",16),
                    ("7-",17),("7",18),("7+",19),
                    ("8-",20),("8",21),("8+",22),
                    ("9-",23),("9",24),("9+",25)]
    g_choices = []  
    for grade in grades_choices:
        g_choices.append((grade[1],grade[0]))

    climbing_grades=models.IntegerField(
        choices=g_choices,
        default=1,)

    protection=models.IntegerField(
        choices=protection_choices,
        default=3)

    topo = models.ImageField("topo", upload_to=upload_to, default='topo/default.jpg')
    def save(self, *args, **kwargs):
        self.tourtype = "Klettern"
        super().save(*args, **kwargs)

class Skitour(Tour):
    def save(self, *args, **kwargs):
        self.tourtype = "Schitour"
        super().save(*args, **kwargs)

class Hochtour(Tour):
    fitness_difficulty = models.CharField(
        max_length=10,
        choices=diff_choices,
        default='schwierig',)
    tech_difficulty = models.CharField(
        max_length=10,
        choices=diff_choices,
        default='schwierig',)
    def save(self, *args, **kwargs):
        if self.tech_difficulty == 'schwierig' or self.fitness_difficulty == 'schwierig':
            self.difficulty = 'schwierig' 
        elif self.tech_difficulty =='mittel' or self.fitness_difficulty == 'mittel':
            self.difficulty = 'mittel'
        else:
            self.difficulty = 'leicht'
            print('heureeeka')

        print(self.difficulty)
        print(self.fitness_difficulty)
        print(self.tech_difficulty)
        self.tourtype = "Hochtour"
        super().save(*args, **kwargs)

class Wandern(Tour):
    def save(self, *args, **kwargs):  
        self.tourtype = "Wandern"
        super().save(*args, **kwargs)

class HikeAndFly(Tour):
    
    def save(self, *args, **kwargs):
        self.tourtype = "Hike and Fly"
        super().save(*args, **kwargs)

