# Generated by Django 3.2.13 on 2022-05-10 15:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CarRental', '0006_auto_20220510_1602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rental_history',
            name='date',
        ),
        migrations.AddField(
            model_name='car_selection',
            name='Location',
            field=models.CharField(default=django.utils.timezone.now, max_length=35),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rental_history',
            name='pickup',
            field=models.CharField(default=django.utils.timezone.now, max_length=35),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rental_history',
            name='returntime',
            field=models.CharField(default=django.utils.timezone.now, max_length=35),
            preserve_default=False,
        ),
    ]