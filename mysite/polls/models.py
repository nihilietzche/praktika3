from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=60)

    def __str__(self):
        return self.category

    class Meta(object):
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Test(models.Model):
    title = models.CharField(max_length=4096)
    visible = models.BooleanField(default=False)
    max_points = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    
    
    def __str__(self):
        return self.title

    class Meta(object):
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'



class Question(models.Model):
    title_test = models.ForeignKey(Test, on_delete=models.DO_NOTHING)
    question_text = models.TextField()
    question_point = models.IntegerField(default = 1)
		
    def __str__(self):
        return self.question_text

    class Meta(object):
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Choice(models.Model):
    choice = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    choice_text = models.TextField()
    choice_point = models.IntegerField(default = 0)
        
    def __str__(self):
        return self.choice_text

    class Meta(object):
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'