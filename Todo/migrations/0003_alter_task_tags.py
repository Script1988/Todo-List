# Generated by Django 4.1.4 on 2022-12-09 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0002_alter_task_datetime_alter_task_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tags',
            field=models.ManyToManyField(related_name='tags', to='Todo.tag'),
        ),
    ]
