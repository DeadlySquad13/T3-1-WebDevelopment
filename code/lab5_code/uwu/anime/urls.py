from django.urls import path

from . import views
from .apps import AnimeConfig

# Namespacing.
app_name = AnimeConfig.name

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:anime_id>/rate/', views.rate, name='rate')
]
