# Generated by Django 3.1 on 2020-10-13 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length=150, verbose_name='Bio'),
        ),
    ]
