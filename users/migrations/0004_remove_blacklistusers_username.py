# Generated by Django 4.1.7 on 2023-03-07 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_blacklistusers_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blacklistusers',
            name='username',
        ),
    ]