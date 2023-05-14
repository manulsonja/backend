from .views import *
from rest_framework.routers import DefaultRouter
from .views import *

app_name = 'touren'

router = DefaultRouter()

router.register('touren', ViewTouren, basename='tour')
router.register('hochtour', ViewHochtouren, basename='hochtour')
router.register('wandern', ViewWandern, basename='wandern')
router.register('schitour', ViewSkitour, basename='skitour')
router.register('hike and fly', ViewHaF, basename='hikeandflz')
router.register('klettern', ViewKlettertour, basename='hikeandflz')

urlpatterns = router.urls
