from django.urls import path
from .views import manage_reporters, manage_issues

urlpatterns = [
    path('reporters/', manage_reporters),
    path('issues/', manage_issues),
]