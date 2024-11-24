"""
URL configuration for myblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path
# from task1.views import *
from myblog.views import *

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', home_page),
#     path('game/', game_page),
#     path('cart/', cart_page),
#     path('sing/', sign_up_by_django),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_list),
    path('view/', post_list_view),
]
