# Generated by Django 2.2 on 2019-04-03 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ToDo.TaskList'),
        ),
    ]