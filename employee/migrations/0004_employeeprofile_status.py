# Generated by Django 5.0.2 on 2024-06-17 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_rename_employee_employeeprofile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeprofile',
            name='status',
            field=models.CharField(choices=[('JN', 'Joined'), ('RG', 'Regular'), ('NA', 'Not Assigned')], default='NA', max_length=10),
        ),
    ]
