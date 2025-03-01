from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('create/', views.contact_create, name='contact_create'),
    path('delete/<int:pk>/', views.contact_delete, name='contact_delete'),
]