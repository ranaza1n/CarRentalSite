# Generated by Django 3.2.13 on 2022-05-05 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarRental', '0002_auto_20220428_0149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car_Selection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=15)),
                ('color', models.CharField(max_length=15)),
                ('vehicle_id', models.CharField(max_length=15)),
                ('seating_capacity', models.CharField(max_length=15)),
                ('rental_rate', models.CharField(max_length=15)),
            ],
        ),
    ]
