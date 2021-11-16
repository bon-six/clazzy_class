from django.urls import path

from .views import CommentAddView, CommentDeleteView, CommentDetailView, CommentUpdateView, HomePageView, QuestionDetailView, VoteResultView,\
        VotingStartView, VotingView, VotedView,\
        CommentDetailView, CommentDeleteView, CommentUpdateView, CommentAddView

urlpatterns = [
    path('question/<int:pk>/result', VoteResultView.as_view(), name='vote_result'),
    path('question/<int:pk>/', QuestionDetailView.as_view(), name='question_detail'),
    path('voting/start/', VotingStartView.as_view(), name='voting_start'),
    path('voting/<int:pk>/', VotingView.as_view(), name='voting'),
    path('voting/done/', VotedView.as_view(), name='voted'),
    path('comment/<int:pk>/del/',CommentDeleteView.as_view(), name='del_comment'),
    path('comment/<int:pk>/edit/',CommentUpdateView.as_view(), name='edit_comment'),
    path('comment/<int:pk>/',CommentDetailView.as_view(), name='view_comment'),
    path('comment/',CommentAddView.as_view(), name='add_comment'),
    path('', HomePageView.as_view(), name='home'),
]