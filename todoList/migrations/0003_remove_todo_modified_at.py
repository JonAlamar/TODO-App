# Generated by Django 4.1.3 on 2022-12-02 21:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoList', '0002_todo_modified_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='modified_at',
        ),
    ]
