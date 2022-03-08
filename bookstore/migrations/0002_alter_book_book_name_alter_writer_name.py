# Generated by Django 4.0.3 on 2022-03-06 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='writer',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
