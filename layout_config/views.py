from .serializers import *
from rest_framework import viewsets
from django.utils import timezone
from layout_config.models import LandingPageLayout
from touren.serializers import TourSerializer
from touren.models import Tour

class ViewNewestTours(viewsets.ModelViewSet):
    queryset = Tour.tourobjects.all()[:5]
    serializer_class = TourSerializer
 
class ViewCurrentTours(viewsets.ModelViewSet):
    time = timezone.now().date()
    month = time.month
    queryset = Tour.tourobjects.filter(season__contains=month).order_by('?')
    serializer_class = TourSerializer

class ViewLandingPage(viewsets.ModelViewSet):
    queryset = LandingPageLayout.objects.all()
    serializer_class = LandingPageSerializer



