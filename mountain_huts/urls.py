from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'huts'

router = DefaultRouter()
router.register('', ViewHut, basename='huette')
urlpatterns = router.urls
