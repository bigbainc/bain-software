from django.contrib import admin
from .models import Question, Category

@admin.register(Question) #this registers the Question model with the admin site
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','question', 'solution1', 'solution2', 'solution3', 'solution4', 'createAt',) #these are the fields that will be displayed in the admin list view
    search_fields = ('question','id',) #these are the fields that will be searchable in the admin interface

@admin.register(Category) #also register the Category model so that it can be managed in the admin interface
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',) #fields to display in admin list view
    search_fields = ('name','id',) #fields that are searchable in admin interface