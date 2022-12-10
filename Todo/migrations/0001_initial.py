# Generated by Django 4.1.4 on 2022-12-09 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('datetime', models.DateField()),
                ('deadline', models.DateField(blank=True, null=True)),
                ('progres', models.BooleanField(default=False)),
                ('tags', models.ManyToManyField(related_name='tag', to='Todo.tag')),
            ],
            options={
                'ordering': ['progres', '-datetime'],
            },
        ),
    ]
