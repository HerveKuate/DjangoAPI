# Generated by Django 2.2 on 2019-04-07 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0002_auto_20190403_1422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='list',
        ),
        migrations.DeleteModel(
            name='ListAccess',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
        migrations.DeleteModel(
            name='TaskList',
        ),
    ]
