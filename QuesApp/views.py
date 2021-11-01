from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import Question

# Create your views here.
class homepage_view(ListView):
    model = Question
    template_name = 'QuesApp/home.html'


class detail_view(DetailView):
    model = Question
    template_name = 'QuesApp/detail.html'