from rest_framework import serializers
from pictures.contrib.rest_framework import PictureField
from blog.models import BlogArticle
from users.serializers import AuthorSerializer

class ArticleSerializer(serializers.ModelSerializer):
        image = PictureField()
        author = serializers.SerializerMethodField()
        def get_author(self,obj):
            author = obj.author 
            return AuthorSerializer(author).data
     
        class Meta:
                fields = ('id','title', 'image','slug','category','author','text','subtitle')
                model = BlogArticle

