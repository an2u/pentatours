# Generated by Django 5.0 on 2024-02-01 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_tripdetail_passengers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tripdetail',
            old_name='Cordinator',
            new_name='Coordinator',
        ),
        migrations.RenameField(
            model_name='tripdetail',
            old_name='location',
            new_name='locations',
        ),
    ]
