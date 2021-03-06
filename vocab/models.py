import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Vocab(models.Model):
    vocabTxt = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.vocabTxt

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)

class Definition(models.Model):
    vocab = models.ForeignKey(Vocab, on_delete=models.CASCADE)
    defTxt = models.TextField()
    wrongC = models.IntegerField(default = 0)

    def __str__(self):
        return self.defTxt
