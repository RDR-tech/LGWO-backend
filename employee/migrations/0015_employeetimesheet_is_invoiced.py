# Generated by Django 5.0.2 on 2024-09-09 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0014_remove_employeetimesheet_timesheet_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeetimesheet',
            name='is_invoiced',
            field=models.BooleanField(default=False),
        ),
    ]
