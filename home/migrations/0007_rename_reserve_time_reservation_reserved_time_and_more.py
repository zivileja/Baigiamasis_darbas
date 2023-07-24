# Generated by Django 4.2.3 on 2023-07-24 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_reservetime_desired_service_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='reserve_time',
            new_name='reserved_time',
        ),
        migrations.RenameField(
            model_name='reservation',
            old_name='service',
            new_name='services',
        ),
        migrations.RenameField(
            model_name='reservetime',
            old_name='num_of_pets',
            new_name='pets_numbers',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='reserved_time',
        ),
    ]