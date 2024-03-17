from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('services/', views.services, name = 'services'),
    path('contact/', views.contacts, name = 'contacts'),
    path('register/', views.register, name = 'register'),
]
