# Generated by Django 2.1.3 on 2018-11-22 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ContestApp', '0002_auto_20181123_0030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challenge',
            name='college_id',
        ),
        migrations.RemoveField(
            model_name='college',
            name='contest_id',
        ),
        migrations.RemoveField(
            model_name='submission_stats',
            name='Challenge_id',
        ),
        migrations.RemoveField(
            model_name='view_stats',
            name='Challenge_id',
        ),
        migrations.DeleteModel(
            name='Challenge',
        ),
        migrations.DeleteModel(
            name='College',
        ),
        migrations.DeleteModel(
            name='Contest',
        ),
        migrations.DeleteModel(
            name='Submission_Stats',
        ),
        migrations.DeleteModel(
            name='View_Stats',
        ),
    ]
