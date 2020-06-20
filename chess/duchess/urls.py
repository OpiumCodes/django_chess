from django.urls import path
from . import views

urlpatterns = [
    path('play/',views.play,name = "play"),
    path('login/',views.login,name = "login"),
    path('register/',views.register,name = "register"),
    path('',views.home,name = "home"),
]