from django.db import models

class Category(models.Model): #model to represent question categories
    name = models.CharField(max_length=50, unique=True) #name of the category, must be unique

    def __str__(self):
        return self.name
class Question(models.Model):#model to represent questions
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='questions') #the current user who created the question
    question = models.CharField(max_length=100) #the text of the question with 100 character limit
    solution1 = models.CharField(max_length=50) #the text of the answers with 50 character limit
    solution2 = models.CharField(max_length=50)
    solution3 = models.CharField(max_length=50)
    solution4 = models.CharField(max_length=50)
    CORRECT_CHOICES = ( #the possible choices for the correct answer
        (1, 'Answer 1'),
        (2, 'Answer 2'),
        (3, 'Answer 3'),
        (4, 'Answer 4'),
    )
    correct_answer = models.PositiveSmallIntegerField(choices=CORRECT_CHOICES, default=1) #the correct answer field as one of the previously defined choices (line 15-20)
    createAt = models.DateTimeField(auto_now_add=True) #timestamp for when the question was created
    category = models.ManyToManyField('Category', related_name='questions', blank=True) #many-to-many relationship with categories meaning there can be multiple categories per question

    def __str__(self):
        return f"Question: '{self.question}'"