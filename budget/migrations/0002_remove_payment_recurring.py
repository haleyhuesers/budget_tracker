# Generated by Django 5.0.2 on 2024-04-29 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='recurring',
        ),
    ]