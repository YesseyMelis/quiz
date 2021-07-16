from django.contrib import admin

from apps.interview.models import Quiz, Question, Variant

admin.site.register((
    Quiz,
    Question,
    Variant
))
