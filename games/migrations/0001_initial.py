# Generated by Django 4.2.11 on 2024-04-10 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]