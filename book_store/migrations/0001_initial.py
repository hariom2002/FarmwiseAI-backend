# Generated by Django 4.2.9 on 2024-01-26 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookStore',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=50)),
                ('ISBN', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]