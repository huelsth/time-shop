from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('book/<int:time_model_id>/', views.book_time, name='book_time'),
]
