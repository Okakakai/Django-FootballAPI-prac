# Generated by Django 3.2 on 2021-12-14 04:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_auto_20211213_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
