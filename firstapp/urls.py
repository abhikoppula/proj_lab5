from django.urls import path
from .views import firstView

urlpatterns = [
    path("", firstView, name="home"),
]