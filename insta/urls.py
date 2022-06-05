from . import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.homepage, name='landing'),
    path('profile/<int:profileId>', views.profile, name='profile'),
    path('user/update/profile', views.update_profile, name='updateprofile'),
]