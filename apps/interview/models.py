from django.contrib.postgres.fields import JSONField
from django.db import models

from apps.account.models import User
from apps.interview import QuestionTypes


class Quiz(models.Model):
    name = models.CharField('Наименование', max_length=100)
    start_date = models.DateTimeField('Дата старта')
    end_date = models.DateTimeField('Дата окончания')
    description = models.TextField('Описание')
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        return self.name


class Question(models.Model):
    body = models.TextField('Текст вопроса')
    question_type = models.CharField(
        'Тип вопроса',
        max_length=100,
        choices=QuestionTypes.choices,
        default=QuestionTypes.SINGLE_VARIANT
    )
    quiz = models.ForeignKey(
        Quiz,
        on_delete=models.SET_NULL,
        null=True,
        related_name='questions'
    )

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.body


class Variant(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='variants')
    text = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'

    def __str__(self):
        return self.text


class UserQuiz(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.SET_NULL, null=True, related_name='users')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='quizzes')
    user_ident = models.IntegerField('Идентификатор пользователя', unique=True)
    answers = JSONField(blank=True, default=dict)

    class Meta:
        verbose_name = 'Опрос пользователя'
        verbose_name_plural = 'Опросы пользователя'

    def __str__(self):
        return f'{self.quiz} {self.user}'
