# Generated by Django 4.2.11 on 2024-04-11 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='slug',
            field=models.CharField(default='elden_ring', max_length=100),
        ),
    ]