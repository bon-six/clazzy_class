from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Question

# Create your views here.
class HomePageView(ListView):
    model = Question
    template_name = 'QuesApp/home.html'


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'QuesApp/detail.html'

class VoteResultView(DetailView):
    model = Question
    template_name = 'QuesApp/result.html'