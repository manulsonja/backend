from django.db import models
from blog.models import BlogArticle
# Create your models here.

class LandingPageLayout(models.Model):
    primary_feature_article =    models.OneToOneField(
        BlogArticle,
        on_delete=models.SET_NULL,
        primary_key=False,
        null=True,
    )