# Generated by Django 2.2.4 on 2021-04-19 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_shell', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='random notes', max_length=200),
        ),
    ]