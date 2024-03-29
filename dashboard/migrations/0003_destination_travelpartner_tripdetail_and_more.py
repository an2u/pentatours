# Generated by Django 5.0 on 2024-02-01 05:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_destinations_travelpartners_tripdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TravelPartner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.IntegerField()),
                ('place', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TripDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cordinator', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('budget', models.IntegerField()),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.destination')),
                ('travel_partner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='dashboard.travelpartner')),
            ],
        ),
        migrations.DeleteModel(
            name='Destinations',
        ),
        migrations.DeleteModel(
            name='TravelPartners',
        ),
        migrations.DeleteModel(
            name='TripDetails',
        ),
    ]
