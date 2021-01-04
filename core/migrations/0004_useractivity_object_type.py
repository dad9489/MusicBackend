# Generated by Django 3.1.2 on 2021-01-04 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210103_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='useractivity',
            name='object_type',
            field=models.CharField(choices=[('TR', 'Track'), ('AR', 'Artist'), ('AL', 'Album'), ('PL', 'Playlist')], default='TR', max_length=2),
        ),
    ]
