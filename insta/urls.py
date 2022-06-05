from . import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.homepage, name='landing'),
   path('user/<int:user_id>', views.profile, name='profile'),
    path('new/profile', views.update_profile, name='update_profile'),
]