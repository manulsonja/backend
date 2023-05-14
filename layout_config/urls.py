from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'layout_config'

router = DefaultRouter()

router.register('newest-tours', ViewNewestTours, basename='newest_tours')
router.register('current-tours', ViewCurrentTours, basename='current_tours')
router.register('manual-content', ViewLandingPage, basename='manual-content')

urlpatterns = router.urls
