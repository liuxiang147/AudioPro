from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/health/', views.health, name='health'),
    path('api/og', views.og_image, name='og_image'),
]
