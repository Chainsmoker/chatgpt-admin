# Generated by Django 4.1.7 on 2023-03-06 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlackListUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=255)),
                ('reason', models.TextField()),
            ],
        ),
    ]
