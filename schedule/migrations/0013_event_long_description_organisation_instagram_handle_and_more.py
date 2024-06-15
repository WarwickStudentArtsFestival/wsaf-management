# Generated by Django 5.0.6 on 2024-05-28 16:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("schedule", "0012_rename_public_description_event_short_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="long_description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="organisation",
            name="instagram_handle",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="organisation",
            name="is_society",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="organisation",
            name="website_name",
            field=models.CharField(blank=True, help_text="Will override website URL label", max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="organisation",
            name="website_url",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]