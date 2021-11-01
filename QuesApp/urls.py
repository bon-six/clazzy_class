from django.urls import path

from .views import homepage_view, detail_view

urlpatterns = [
    path('question/<int:pk>/', detail_view.as_view(), name='question_detail'),
    path('', homepage_view.as_view(), name='home'),
]