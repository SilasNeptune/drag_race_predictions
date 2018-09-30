# Generated by Django 2.1.1 on 2018-09-30 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('queens', '0001_initial'),
        ('appearances', '0001_initial'),
        ('episodes', '0003_episode_season'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='queens',
            field=models.ManyToManyField(through='appearances.Appearance', to='queens.Queen'),
        ),
    ]
