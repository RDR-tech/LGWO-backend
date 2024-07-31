# Generated by Django 5.0.2 on 2024-07-31 18:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_employeetimesheet_is_verified_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(verbose_name='Order')),
                ('name', models.CharField(max_length=100, verbose_name='Cycle Name')),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeCycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cycle', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cycle', to='employee.cycle')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cycles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EmplpoyeeLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(max_length=100)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='logs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
