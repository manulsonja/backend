from .serializers import *
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from parking.models import Parking
from rest_framework import pagination

class CustomPagination(pagination.CursorPagination):
    page_size = 12
    cursor_query_param = 'c'
    ordering = '-created'

class ViewParking(viewsets.ModelViewSet):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer
    pagination_class = CustomPagination
    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Parking, slug=item)
    