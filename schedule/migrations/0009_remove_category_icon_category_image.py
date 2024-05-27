# Generated by Django 5.0.6 on 2024-05-27 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0008_event_logo_organisation_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='icon',
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/category-icons/'),
        ),
    ]
