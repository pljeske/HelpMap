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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from HelpMap import settings
from registration import views as regviews
from map import views as mapviews
from social import views as socialviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mapviews.index, name="index"),
    path('account/login/', regviews.do_login, name="login"),
    path('account/register/', regviews.do_register, name="register"),
    path('account/logout/', regviews.do_logout, name="logout"),
    path('info/', mapviews.get_info, name="who"),
    path('offer/<int:offer_id>/', mapviews.show_help_point, name="offer"),
    path('map/', mapviews.map, name="map"),
    path('map/offer_help/', mapviews.new_help_point, name="add-point"),
    path('map/delete/<int:point_id>', mapviews.delete_help_point, name="delete-point"),
    path('messages/', socialviews.show_messages, name="received-messages"),
    path('messages/<int:user_id>/', socialviews.message_handler, name="conversation"),
    path('profile/', socialviews.show_profile, name="profile"),
    path('profile/<int:user_id>', socialviews.show_other_profile, name="other-profile"),
    path('profile/change/', regviews.change_profile, name="change-profile"),
    path('api/messages/<int:user_id>', socialviews.get_messages_rest, name="api"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
