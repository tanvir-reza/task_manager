# Generated by Django 5.0.1 on 2024-01-27 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='images',
        ),
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
        migrations.DeleteModel(
            name='Task_image',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
