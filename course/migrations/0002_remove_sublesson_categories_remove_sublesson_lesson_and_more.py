# Generated by Django 4.2.10 on 2024-02-25 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sublesson',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='sublesson',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='categories',
        ),
        migrations.AlterField(
            model_name='lesson',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='SubLesson',
        ),
    ]