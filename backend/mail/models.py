from django.db import models


class Mail(models.Model):
    name = models.CharField(max_length=24)
    question = models.CharField(max_length=800)
    def __str__(self):
        return self.question
