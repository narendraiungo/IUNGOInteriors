from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from LIstings import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name='home'),
    path('register/', views.usercreation, name='register'),
    path('ajax/load_categories/', views.load_categories, name='ajax_load_categories'),
    path('accounts/login/', views.userpage, name='userpage'),
    path('accounts/login/userpage/', views.userauthentication, name='userauthentication'),
    path('userlist/<str:user_type>/',views.user_list, name='user_list'),
    path('searchposts/', views.searchposts,name='searchposts'),
]