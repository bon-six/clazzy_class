from django.urls import path, re_path
from .views import SignupView

urlpatterns = [
    path('',SignupView.as_view(),name='my_signup'),
]