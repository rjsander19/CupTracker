from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cups/', views.cups_index, name='index'),
    path('cups/<int:cup_id>/', views.cups_detail, name='detail'),
    path('cups/create/', views.CupCreate.as_view(), name='cups_create'),
    path('cups/<int:pk>/update/', views.CupUpdate.as_view(), name='cups_update'),
    path('cups/<int:pk>/delete/', views.CupDelete.as_view(), name='cups_delete'),
    path('cups/<int:cup_id>/add_use/', views.add_use, name='add_use'),
]