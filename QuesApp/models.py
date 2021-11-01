from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

class Choice (models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    def __str__(self):
        return self.choice_text

class Vote(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    voter_name = models.CharField(max_length=100)
    vote_data = models.DateTimeField('date voted')
    def __str__(self):
        return self.voter_name+ ' at '+str(self.vote_data)