from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'blog'

router = DefaultRouter()
router.register('articles', ViewArticles, basename='articles')

urlpatterns = router.urls
