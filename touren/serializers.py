from rest_framework import serializers
from touren.models import Tour, Hochtour, Wandern, Klettertour, HikeAndFly, Skitour
from pictures.contrib.rest_framework import PictureField
from pictures.contrib.rest_framework import PictureField
from users.serializers import AuthorSerializer

class PictureSerializer(serializers.Serializer):
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    image = PictureField()


#FIELDS FOR DETAIL VIEW WITHOUT SPECIFICS -- BELONGS TO TOURDETAILSERIALIZER
GLOBAL_FIELDS = ('id', 'title', 'text', 'tourtype', 'rating','author', 'created',
        'profile_pk','image','slug','season','offseason','geojson_track','starting_pnt',
        'photoalbum','tour_duration','distance','elevation_values','steps', 'elevation_gain')

class TourSerializer(serializers.ModelSerializer):
        image = PictureField()
        starting_pnt = serializers.SerializerMethodField()
        author = serializers.SerializerMethodField()
     
        def get_author(self,obj):
                author = obj.author
                return AuthorSerializer(author).data
        def get_starting_pnt(self, obj):
                ls = obj.track
                start = ls[0]
                return start
        class Meta:
                fields = ('id', 'title', 'text', 'tourtype', 'rating','author', 'created','image','slug',
                'track','starting_pnt','subtitle','tour_duration','distance','difficulty','season','elevation_values','steps')
                model = Tour

class TourDetailSerializer(TourSerializer):
        profile_pk = serializers.SerializerMethodField()
        photoalbum = serializers.SerializerMethodField()
        image = PictureField()
      
        def get_photoalbum(self,obj):
                return PictureSerializer(obj.album.all(), many=True).data 
        def get_author_name(self,obj):
                return obj.author.user_name
     

        def get_profile_pk(self,obj):
                return obj.author.profile.pk
    
class HochtourSerializer(TourDetailSerializer):
     class Meta:
        fields = GLOBAL_FIELDS
        model = Hochtour

class WandernSerializer(TourDetailSerializer):
        class Meta:
                fields = GLOBAL_FIELDS
                model = Wandern

class KlettertourSerializer(TourDetailSerializer):
     class Meta:
        fields = GLOBAL_FIELDS
        model = Klettertour

class HikeAndFlySerializer(TourDetailSerializer):
     class Meta:
        fields = GLOBAL_FIELDS
        model = HikeAndFly

class SkitourSerializer(TourDetailSerializer):
     class Meta:
        fields = GLOBAL_FIELDS
        model = Skitour