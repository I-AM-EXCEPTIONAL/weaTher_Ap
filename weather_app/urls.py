
from django.urls import path
from . import views
from .views import custom_csrf_failure_view


urlpatterns = [
    path('', views.home, name='home')
    path('csrf-failure/', custom_csrf_failure_view, name='csrf_failure'),
]
