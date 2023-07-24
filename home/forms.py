from django.contrib.auth import get_user_model
from .models import Profile, PetService, ReserveTime
from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=150)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=commit)
        Profile.objects.get_or_create(user=user)
        return user


class ProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=150)

    class Meta:
        model = Profile
        fields = ()


class PetServiceForm(forms.ModelForm):
    class Meta:
        model = PetService
        fields = ['title', 'description']


class ReservationForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.ChoiceField(choices=ReserveTime.TIME_CHOICES)
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=150)
    services = forms.ModelMultipleChoiceField(
        queryset=PetService.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    PET_TYPE_CHOICES = (
        ('dog', 'Dog'),
        ('cat', 'Cat'),
        ('reptile', 'Reptile'),
        ('fish', 'Fish'),
    )
    pets_type = forms.ChoiceField(choices=PET_TYPE_CHOICES)

    class Meta:
        model = ReserveTime
        fields = ['name', 'email', 'pets_type', 'pets_numbers', 'address', 'date', 'time', 'services']
