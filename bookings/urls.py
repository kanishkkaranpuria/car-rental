from django.urls import path
from .views import CreateBookingView



urlpatterns = [
    path('', CreateBookingView.as_view()),
]