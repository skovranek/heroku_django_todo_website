# Generated by Django 4.2.4 on 2023-09-29 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_alter_category_user_alter_motto_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='user',
            field=models.CharField(max_length=36),
        ),
        migrations.AlterField(
            model_name='motto',
            name='user',
            field=models.CharField(max_length=36),
        ),
        migrations.AlterField(
            model_name='question',
            name='user',
            field=models.CharField(max_length=36),
        ),
        migrations.AlterField(
            model_name='task',
            name='user',
            field=models.CharField(max_length=36),
        ),
    ]
