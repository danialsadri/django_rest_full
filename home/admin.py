from django.contrib import admin
from .models import Person, Question, Answer


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'email']
    list_filter = ['age']
    search_fields = ['name']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'slug', 'created', 'updated']
    list_filter = ['created', 'updated']
    search_fields = ['title']
    prepopulated_fields = {'slug': ['title']}


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['user', 'question', 'created', 'updated']
    list_filter = ['created', 'updated']
    search_fields = ['body']
