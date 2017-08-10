from django.db import models

#Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=500)
    theme = models.CharField(max_length=500)
    result = models.IntegerField(default=0)

    def __str__(self):
        return self.name



class Question(models.Model):
    test = models.ForeignKey(Test)
    name = models.CharField(max_length=500)
    answer_1 = models.CharField(max_length=100)
    answer_2 = models.CharField(max_length=100)
    answer_true = models.CharField(max_length=100)
    result = models.IntegerField(default=0)

    def true_answer(self,answer):
        if self.answer_true == answer:
            self.result += 1
            return self.result




    def __str__(self):
        return self.name
