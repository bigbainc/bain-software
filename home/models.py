from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=100)
    solution1 = models.CharField(max_length=50)
    solution2 = models.CharField(max_length=50)
    solution3 = models.CharField(max_length=50)
    solution4 = models.CharField(max_length=50)

    def __str__(self):
        return f"Question: '{self.question}'"