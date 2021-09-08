from django.contrib import admin
from .models import Test, Question, Choice, Category

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1


class TestAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'visible',
        'max_points',
        'category',
    )
    inlines = [
    QuestionInline,
    ]

class  QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'question_text',
        'question_point',
    )
    inlines = [
    ChoiceInline,
    ]

admin.site.register(Test, TestAdmin)
admin.site.register(Category)
admin.site.register(Question, QuestionAdmin)
