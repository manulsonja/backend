from rest_framework import serializers
from blog.serializers import ArticleSerializer

class LandingPageSerializer(serializers.Serializer):
        primary_feature_article_pk = serializers.SerializerMethodField()
        def get_primary_feature_article_pk(self, obj):
               return ArticleSerializer(obj.primary_feature_article).data
        