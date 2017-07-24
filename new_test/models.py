from django.db import models

# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=500)
    theme = models.CharField(max_length=500)
    question_1 = models.CharField(max_length=500, blank=True)



class Question(models.Model):
    test = models.ForeignKey(Test)
    name = models.CharField(max_length=500)
    answer_1 = models.CharField(max_length=100, blank=True)
    answer_2 = models.CharField(max_length=100, blank=True)
    answer_3 = models.CharField(max_length=100, blank=True)
