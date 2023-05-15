from django.contrib.gis.db import models
from tinymce import models as tinymce_models
from django.utils import timezone
from users.models import NewUser 
from pictures.models import PictureField
from django.utils.text import slugify
from pictures.models import PictureField

def upload_to(instance, filename):
    return 'huts/{filename}'.format(filename=filename)

class BlogArticle(models.Model): 
    
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),)
    title = models.CharField(max_length=30)   
    subtitle = models.CharField(max_length=500, null=True)
    image = PictureField("Image", upload_to=upload_to, default='tour/default.jpg', aspect_ratios=["16/9"])
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        NewUser, on_delete=models.CASCADE, related_name='articles',) 
    status = models.CharField(
        max_length=10, choices=options, default='published')

    slug = models.SlugField(max_length=250, unique_for_date='published', editable=False, null=True)
    class Meta:
        ordering = ('-published',)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Image(models.Model):
    image = PictureField("Image", upload_to=upload_to, default='tour/default.jpg',  aspect_ratios=["16/9"]) 
    parent = models.ForeignKey(BlogArticle,on_delete=models.CASCADE,related_name="album")
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class ContentChunk(models.Model):
    image = PictureField("Image", upload_to=upload_to, default='tour/default.jpg',  aspect_ratios=["16/9"], blank=True) 
    image_subtext =  models.CharField(max_length=500, null=True, blank=True)
    heading = models.CharField(max_length=500, null=True, blank=True)
    text =  models.TextField(blank=True)
    parent = models.ForeignKey(BlogArticle,on_delete=models.CASCADE,related_name="content")
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


