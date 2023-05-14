from rest_framework import serializers
from pictures.contrib.rest_framework import PictureField
from mountain_huts.models import MountainHut
from users.serializers import AuthorSerializer
from touren.serializers import PictureSerializer
from django.utils import timezone
from pprint import pprint

class HutSerializer(serializers.ModelSerializer):
        
        gallery = serializers.SerializerMethodField()
        image = PictureField()
        author = serializers.SerializerMethodField()
        position = serializers.SerializerMethodField()
        open = serializers.SerializerMethodField()


        def get_open(self, obj):
                time = timezone.now()
                month = str(time.month)

                if month in obj.season:
                        return 2
                elif month in obj.offseason:
                        return 1
                else:
                        return 0

        def get_position(self, obj):
                pos = obj.position 
                try:
                        lon = pos[0]
                        lat = pos[1]
                        return [lat, lon]
                except:
                        return None
        def get_author(self,obj):
               author = obj.author
               return AuthorSerializer(author).data
   
        def get_gallery(self,obj):
                return PictureSerializer(obj.gallery.all(), many=True).data 
        
        class Meta:
                fields = ('id', 'name', 'position','image','text','overnight','altitude','hut_type','rating','slug','subtitle',
                'telephone','website','email','slug','gallery','author','season','offseason','open')
                model = MountainHut