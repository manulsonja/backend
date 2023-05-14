"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from pictures.conf import get_settings
from django.views.generic import TemplateView




urlpatterns = [
    path('admin/', admin.site.urls),
############### plugins ####################
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.social.urls')),
    path('tinymce/', include('tinymce.urls')),
############### apps #######################
    path('api/',     include('api.urls')),
    path('touren/', include('touren.urls')),
    path('huts/', include('mountain_huts.urls')),
    path('parking/', include('parking.urls')),
    path('blog/', include('blog.urls')),
    path('layout-widgets/', include('layout_config.urls')),
    path('user/', include('users.urls', namespace='users')), 
]

if get_settings().USE_PLACEHOLDERS:
    urlpatterns += [
        path("media/posts/", include("pictures.urls")),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]





 