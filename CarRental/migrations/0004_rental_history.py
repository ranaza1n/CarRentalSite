# Generated by Django 3.2.13 on 2022-05-09 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarRental', '0003_car_selection'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=15)),
                ('memberID', models.CharField(max_length=15)),
                ('vehicle_id', models.CharField(max_length=15)),
                ('date', models.DateField()),
            ],
        ),
    ]
