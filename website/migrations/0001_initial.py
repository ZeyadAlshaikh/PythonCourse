# Generated by Django 5.1.4 on 2024-12-18 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=5, verbose_name='title')),
                ('body', models.TextField(max_length=500, verbose_name='body')),
            ],
        ),
    ]
