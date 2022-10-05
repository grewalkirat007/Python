from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.getData, name='getData'),
]