from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login,name="login"),
    path('getdata', views.getdata,name="getdata"),
    path('home',views.home,name="home"),
    path('contacts',views.contacts,name="contacts"),
    path('services',views.services,name="services"),
    path('signup',views.signup,name="signup"),
    path('logout',views.logout,name="logout"),
]