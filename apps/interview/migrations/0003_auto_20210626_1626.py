# Generated by Django 2.2.10 on 2021-06-27 16:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0002_auto_20210626_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Дата старта'),
        ),
    ]
