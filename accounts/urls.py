from .views import index, test_email
from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('protected-route/', index),
    path('test-email/', test_email, name='test-email')
]
