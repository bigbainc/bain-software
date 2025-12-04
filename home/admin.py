from django.contrib import admin
from .models import Question, Category

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','question', 'solution1', 'solution2', 'solution3', 'solution4', 'createAt',)
    search_fields = ('question','id',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name','id',)