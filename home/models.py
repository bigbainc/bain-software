from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
class Question(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='questions')
    question = models.CharField(max_length=100)
    solution1 = models.CharField(max_length=50)
    solution2 = models.CharField(max_length=50)
    solution3 = models.CharField(max_length=50)
    solution4 = models.CharField(max_length=50)
    createAt = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField('Category', related_name='questions', blank=True)

    def __str__(self):
        return f"Question: '{self.question}'"