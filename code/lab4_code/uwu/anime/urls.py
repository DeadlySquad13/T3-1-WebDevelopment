from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:anime_id>/', views.detail, name='detail'),
    path('<int:anime_id>/results/', views.results, name='results'),
    path('<int:anime_id>/rate/', views.rate, name='rate')
]
