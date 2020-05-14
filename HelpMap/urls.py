"""HelpMap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from registration import views as regviews
from map import views as mapviews
from social import views as socialviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mapviews.index, name="index"),
    path('index2/', mapviews.index_old, name="index2"),
    path('account/login/', regviews.do_login, name="login"),
    path('account/register/', regviews.do_register, name="register"),
    path('account/logout/', regviews.do_logout, name="logout"),
    path('who/', mapviews.who, name="who"),
    path('map/help/', mapviews.create_entry, name="create-entry"),
    path('map/add_point/', mapviews.add_help_point, name="add-point"),
    path('messages/received/', socialviews.show_messages, name="received-messages"),
]
