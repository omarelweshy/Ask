# Generated by Django 3.1 on 2020-10-16 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_online'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='online',
        ),
    ]