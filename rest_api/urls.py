from django.urls import path
from . import views


urlpatterns = [
    path('get_stocks/', views.get_stocks, name='available stocks'),
]