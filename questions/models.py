from django.db import models
from django.utils import timezone
import datetime
# Create your models here.

class Question(models.Model):
    questions = models.CharField("问题", max_length=1000)
    options = models.CharField("选项", max_length=1000)
    result =  models.CharField("答案", max_length=1000)
    def __str__(self):
        return self.question_text


class Meta:
    verbose_name = '题目'
    verbose_name_plural = '题目'