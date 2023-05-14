from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'parking'

router = DefaultRouter()
router.register('', ViewParking, basename='parking')

urlpatterns = router.urls
