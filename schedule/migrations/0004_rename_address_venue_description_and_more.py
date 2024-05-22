# Generated by Django 5.0.6 on 2024-05-22 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_event_data_collected'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venue',
            old_name='address',
            new_name='description',
        ),
        migrations.AddField(
            model_name='venue',
            name='campus_map_url',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='slug',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]