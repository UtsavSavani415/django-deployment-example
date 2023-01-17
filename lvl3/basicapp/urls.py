
from django.urls import path
from . import views

app_name = 'basicapp'
urlpatterns = [
    path('', views.index, name="index"),
    path('registration/', views.registration, name="registration"),
    path('user_login/', views.user_login, name="user_login"),
    path('logout/', views.user_logout, name="logout"),
    path('special/', views.special, name="special"),

]