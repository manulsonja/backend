from django.contrib.gis.db import models
from tinymce import models as tinymce_models
from django.utils import timezone
from users.models import NewUser 
from pictures.models import PictureField
from django.utils.text import slugify


def upload_to(instance, filename):
    return 'huts/{filename}'.format(filename=filename)

class BlogArticle(models.Model): 
    category = (
        ('alm', 'Alm'),
        ('huette', 'Huette'),
        ('gasthof', 'Gasthof'),
        ('sonstige', 'Sonstige'),  
        )

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),)
    title = models.CharField(max_length=30)   
    subtitle = models.CharField(max_length=500, null=True)
    text =  tinymce_models.HTMLField()
    image = PictureField("Image", upload_to=upload_to, default='tour/default.jpg', aspect_ratios=["16/9"])
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        NewUser, on_delete=models.CASCADE, related_name='articles',) 
    status = models.CharField(
        max_length=10, choices=options, default='published')
    
    category = models.CharField(
        max_length=10, choices=category, default='Huette')
    slug = models.SlugField(max_length=250, unique_for_date='published', editable=False, null=True)
    class Meta:
        ordering = ('-published',)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

