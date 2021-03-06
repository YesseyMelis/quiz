# Generated by Django 2.2.10 on 2021-06-27 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Наименование')),
                ('start_date', models.DateTimeField(editable=False, verbose_name='Дата старта')),
                ('end_date', models.DateTimeField(verbose_name='Дата окончания')),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(blank=True, verbose_name='Текст вопроса')),
                ('question_type', models.CharField(choices=[('TEXT', 'TEXT'), ('SINGLE_VARIANT', 'SINGLE_VARIANT'), ('MULTIPLE_VARIANT', 'MULTIPLE_VARIANT')], default='SINGLE_VARIANT', max_length=100, verbose_name='Тип вопроса')),
                ('quiz', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='questions', to='interview.Quiz')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
    ]
