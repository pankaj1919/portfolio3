# Generated by Django 3.0.5 on 2020-05-07 15:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume_study',
            name='title',
        ),
        migrations.RemoveField(
            model_name='work_history',
            name='title',
        ),
    ]