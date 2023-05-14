from rest_framework import serializers
from pictures.contrib.rest_framework import PictureField
from .models import Parking
from touren.serializers import PictureSerializer


class ParkingSerializer(serializers.ModelSerializer):        
        image = PictureField()
        gallery = serializers.SerializerMethodField()
        position = serializers.SerializerMethodField()

        def get_position(self, obj):
                pos = obj.position 
                try:
                        lon = pos[0]
                        lat = pos[1]
                        return [lat, lon]
                except:
                        return None
                
        def get_gallery(self,obj):
                return PictureSerializer(obj.gallery.all(), many=True).data 
        class Meta:
                fields = ('parkingtype', 'name','estate','ground_type','capacity', 'short_text','position','image','toilet','fees','slug','text','gallery')
                model = Parking
