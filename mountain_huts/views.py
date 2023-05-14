from .serializers import *
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework import pagination


class CustomPagination(pagination.CursorPagination):
    page_size = 12
    cursor_query_param = 'c'
    ordering = '-created'

class ViewHut(viewsets.ModelViewSet):
    queryset = MountainHut.objects.all()
    serializer_class = HutSerializer
    pagination_class=CustomPagination
   # Define Custom Queryset
    def get_queryset(self):
        try:
            huttypes = self.request.query_params.get('huttypes', None)
            huttypes = huttypes.split(',')
            print(huttypes)

            if huttypes==[""]:
                return  
            qs = MountainHut.objects.filter(hut_type__in=huttypes)
        except:
            qs = MountainHut.objects.all()
            print('exception api/views.py line 54 Probably insufficient or no query params provided but required for filtering in django')
        return qs
    
    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(MountainHut, slug=item)
    