"""MusicBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path

from core.routes.login import *
from core.routes.sheets import *
from core.routes.recommendations import *
from core.routes.profile import *
from core.routes.interactions import interaction, get_liked_songs
from core.routes.user_profile import create_profile
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('torch/', test_torch),
    path('recommendations/', get_recommendations),
    path('profile/', get_profile),
    path('interaction/', csrf_exempt(interaction)),
    path('liked/', get_liked_songs),
    path('createprofile/', create_profile),
]
