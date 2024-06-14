# Generated by Django 5.0.6 on 2024-07-15 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('birthday', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
    ]
