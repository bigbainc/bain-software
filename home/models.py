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
    CORRECT_CHOICES = (
        (1, 'Answer 1'),
        (2, 'Answer 2'),
        (3, 'Answer 3'),
        (4, 'Answer 4'),
    )
    correct_answer = models.PositiveSmallIntegerField(choices=CORRECT_CHOICES, default=1)
    createAt = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField('Category', related_name='questions', blank=True)

    def __str__(self):
        return f"Question: '{self.question}'"