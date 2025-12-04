from django.contrib import admin
from .models import Question

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','question', 'solution1', 'solution2', 'solution3', 'solution4', 'createAt',)
    search_fields = ('question','id',)