from django.urls import path
from .views import CarsDisplayView



urlpatterns = [
    path('', CarsDisplayView.as_view()),
]