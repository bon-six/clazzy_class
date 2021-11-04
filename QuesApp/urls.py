from django.urls import path

from .views import HomePageView, QuestionDetailView, VoteResultView

urlpatterns = [
    path('question/<int:pk>/result', VoteResultView.as_view(), name='vote_result'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question_detail'),
    path('', HomePageView.as_view(), name='home'),
]