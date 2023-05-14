from touren.models import *
from .serializers import *
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from blog.models import BlogArticle

class ViewArticles(viewsets.ModelViewSet):
    queryset = BlogArticle.objects.all()
    serializer_class = ArticleSerializer
    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(BlogArticle, slug=item)
 
