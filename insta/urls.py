from . import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.homepage, name='landing'),
    path('search/', views.search_results, name='search_results'),
    path('user/<int:user_id>', views.profile, name='profile'),
    path('user/add/image', views.add_image, name='addimage'),
    path('user/update/profile', views.update_profile, name='updateprofile'),
    path('post/<int:image_id>',views.single_image,name='singleimage'),
]