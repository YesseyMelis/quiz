# Generated by Django 2.2.10 on 2021-07-16 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0008_auto_20210715_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variant',
            name='correct',
        ),
    ]
