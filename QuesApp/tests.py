from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question


# Create your tests here.

class QuestionAppTest(TestCase):
    def setUp(self):
        question = Question.objects.create(question_text='Your location?', pub_date = timezone.now())
        question.save()

    def test_detail_view(self):
        response = self.client.get(reverse('question_detail', args=[1]))
        self.assertEqual(response.status_code, 200)