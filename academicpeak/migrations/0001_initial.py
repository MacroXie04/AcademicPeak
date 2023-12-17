# Generated by Django 5.0 on 2023-12-17 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('university_id', models.IntegerField(primary_key=True, serialize=False)),
                ('university_rank', models.IntegerField()),
                ('university_name', models.CharField(max_length=30)),
                ('university_country', models.CharField(max_length=30)),
                ('university_global_score', models.IntegerField()),
                ('university_enrollment', models.IntegerField()),
                ('university_link', models.CharField(max_length=100)),
                ('university_photo_link', models.CharField(max_length=100)),
            ],
        ),
    ]
