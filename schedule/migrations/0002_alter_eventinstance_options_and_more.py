# Generated by Django 5.0.6 on 2024-05-21 19:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("schedule", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="eventinstance",
            options={"verbose_name": "Schedule Item", "verbose_name_plural": "Schedule Items"},
        ),
        migrations.RenameField(
            model_name="event",
            old_name="description",
            new_name="public_description",
        ),
        migrations.AddField(
            model_name="event",
            name="org_notes",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="event",
            name="tech_notes",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="eventinstance",
            name="published",
            field=models.BooleanField(default=False),
        ),
    ]