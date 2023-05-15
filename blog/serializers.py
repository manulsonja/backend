from rest_framework import serializers
from pictures.contrib.rest_framework import PictureField
from blog.models import BlogArticle, ContentChunk
from users.serializers import AuthorSerializer

class ArticlePicture(serializers.Serializer):
    image = PictureField()

class PictureSerializer(serializers.Serializer):
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    image = PictureField()

class ContentSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self,obj):
          if(obj.image):
                return ArticlePicture(obj).data
          else:
                return None

    class Meta:
                fields = ('image','heading','text','image_subtext')
                model = ContentChunk

class ArticleSerializer(serializers.ModelSerializer):
        image = PictureField()
        author = serializers.SerializerMethodField()
        photoalbum = serializers.SerializerMethodField()
        content = serializers.SerializerMethodField()

        def get_author(self,obj):
            author = obj.author 
            return AuthorSerializer(author).data
        def get_photoalbum(self,obj):
            return PictureSerializer(obj.album.all(), many=True).data 
        def get_content(self,obj):
            return ContentSerializer(obj.content.all(), many=True).data 
     
     
        class Meta:
                fields = ('id','title', 'image','slug','author','subtitle','content', 'photoalbum')
                model = BlogArticle

