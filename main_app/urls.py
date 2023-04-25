from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cups/', views.cups_index, name='index'),
    path('cups/<int:cup_id>/', views.cups_detail, name='detail'),
]