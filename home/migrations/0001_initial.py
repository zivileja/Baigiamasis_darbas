# Generated by Django 4.2.3 on 2023-07-24 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PetService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='service_photos/')),
            ],
        ),
        migrations.CreateModel(
            name='ReserveTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pets_type', models.CharField(max_length=50)),
                ('pets_numbers', models.FloatField()),
                ('address', models.CharField(default='', max_length=150)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('preferred_service', models.CharField(default='', max_length=100)),
                ('time_choice', models.CharField(choices=[('08:00', '08:00 AM'), ('08:30', '08:30 AM'), ('09:00', '09:00 AM'), ('09:30', '09:30 AM'), ('10:00', '10:00 AM'), ('10:30', '10:30 AM'), ('11:00', '11:00 AM'), ('11:30', '11:30 AM'), ('12:00', '12:00 AM'), ('12:30', '12:30 AM'), ('13:00', '13:00 AM'), ('13:30', '13:30 AM'), ('14:00', '14:00 AM'), ('14:30', '14:30 AM'), ('15:00', '15:00 AM'), ('15:30', '15:30 AM'), ('16:00', '16:00 AM'), ('16:30', '16:30 AM'), ('17:00', '17:00 AM'), ('17:30', '17:30 AM'), ('18:00', '18:00 AM'), ('18:30', '18:30 AM'), ('19:00', '19:00 AM'), ('19:30', '19:30 AM')], default='08:00', max_length=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserved_time', models.DateTimeField()),
                ('services', models.ManyToManyField(to='home.petservice')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(default='', max_length=150)),
                ('preferred_service', models.ManyToManyField(blank=True, to='home.petservice')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]