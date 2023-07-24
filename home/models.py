from django.db import models
from django.contrib.auth.models import User


class AboutContent(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    objects = models.Manager()

    def __str__(self):
        return self.title


class PetService(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='service_photos/', blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.title


class ReserveTime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet_type = models.CharField(max_length=50)
    pets_numbers = models.FloatField()
    address = models.CharField(max_length=150, default='')
    date = models.DateField()
    time = models.TimeField()
    desired_service = models.ManyToManyField(PetService, blank=True)
    objects = models.Manager()

    TIME_CHOICES = (
        ('08:00', '08:00 AM'),
        ('08:30', '08:30 AM'),
        ('09:00', '09:00 AM'),
        ('09:30', '09:30 AM'),
        ('10:00', '10:00 AM'),
        ('10:30', '10:30 AM'),
        ('11:00', '11:00 AM'),
        ('11:30', '11:30 AM'),
        ('12:00', '12:00 PM'),
        ('12:30', '12:30 PM'),
        ('13:00', '13:00 PM'),
        ('13:30', '13:30 PM'),
        ('14:00', '14:00 PM'),
        ('14:30', '14:30 PM'),
        ('15:00', '15:00 PM'),
        ('15:30', '15:30 PM'),
        ('16:00', '16:00 PM'),
        ('16:30', '16:30 PM'),
        ('17:00', '17:00 PM'),
        ('17:30', '17:30 PM'),
        ('18:00', '18:00 PM'),
        ('18:30', '18:30 PM'),
        ('19:00', '19:00 PM'),
        ('19:30', '19:30 PM')
    )

    time_choice = models.CharField(max_length=5, choices=TIME_CHOICES, default='08:00')

    def __str__(self):
        return f"Reservation for {self.user} on {self.date} at {self.time}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=150, default='')
    desired_service = models.ManyToManyField(PetService, blank=True)
    objects = models.Manager()

    def __str__(self):
        return f'{self.user.username} Profile'

    def get_reservations(self):
        return Reservation.objects.filter(user=self.user)


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reserved_time = models.DateTimeField()
    services = models.ManyToManyField(PetService)
    objects = models.Manager()

    def get_services_names(self):
        return ", ".join(str(service) for service in self.services.all())

    def __str__(self):
        return f"Reservation for {self.user} on {self.reserved_time} with services: {self.get_services_names()}"
