# Generated by Django 2.1.3 on 2018-11-22 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge_id', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_id', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_id', models.IntegerField(max_length=20)),
                ('hacker_id', models.IntegerField(max_length=20)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Submission_Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_submission', models.IntegerField(max_length=10)),
                ('total_accepted_submissions', models.IntegerField(max_length=10)),
                ('Challenge_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ContestApp.Challenge')),
            ],
        ),
        migrations.CreateModel(
            name='View_Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_view', models.IntegerField(max_length=10)),
                ('total_unique_view', models.IntegerField(max_length=10)),
                ('Challenge_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ContestApp.Challenge')),
            ],
        ),
        migrations.AddField(
            model_name='college',
            name='contest_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ContestApp.Contest'),
        ),
        migrations.AddField(
            model_name='challenge',
            name='college_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ContestApp.College'),
        ),
    ]
