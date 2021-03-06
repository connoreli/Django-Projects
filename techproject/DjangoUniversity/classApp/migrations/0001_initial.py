# Generated by Django 4.0.4 on 2022-04-24 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Intro to Computer Science', 'Intro to Computer Science'), ('Python Programming', 'Python Programming'), ('App Creation', 'App Creation')], max_length=60)),
                ('course_number', models.IntegerField(default=0)),
                ('instructor_name', models.TextField(blank=True, default='', max_length=60)),
                ('duration', models.FloatField(default=0.0)),
            ],
        ),
    ]
