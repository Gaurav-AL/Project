from django.urls import path

from . import views

urlpatterns = [
    path('recharge',views.Recharge,name="Recharge"),
    path('payment',views.payment,name="payment"),
    path('process',views.process,name="process"),
]


