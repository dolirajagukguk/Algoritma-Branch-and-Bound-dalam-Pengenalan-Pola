from django.urls import path
from . import views

urlpatterns = [
    path('find_patterns/', views.find_patterns, name='find_patterns'),
]