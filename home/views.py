from datetime import datetime
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import UpdateView
from .forms import CustomUserCreationForm, ProfileUpdateForm, PetServiceForm, ReservationForm
from .models import Profile, AboutContent, PetService, Reservation


def home(request):
    about_content = AboutContent.objects.first()
    return render(request, 'home.html', {'about_content': about_content})


class SignUpView(generic.CreateView):
    model = get_user_model()
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        if not hasattr(self.object, 'profile'):
            Profile.objects.create(user=self.object)
            messages.success(self.request, 'Profile created successfully')
            return response
        else:
            messages.warning(self.request, 'Profile already exists')
            return redirect(reverse_lazy('login'))


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('home:profile')
    else:
        if not hasattr(request.user, 'profile'):
            Profile.objects.create(user=request.user)
        form = ProfileUpdateForm(instance=request.user.profile)
    reservations = request.user.profile.get_reservations()

    return render(request, 'profile.html', {'form': form, 'user_profile': request.user.profile,
                                            'reservations': reservations})


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'profile_update.html'
    success_url = '/profile/'


def services(request):
    services = PetService.objects.all()
    return render(request, 'services.html', {'services': services})


def add_pet_service(request):
    if request.method == 'POST':
        form = PetServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pet_service_list')
    else:
        form = PetServiceForm()
    return render(request, 'add_pet_service.html', {'form': form})


@login_required
def reservetime(request):
    user_profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            date = form.cleaned_data['date']
            time_choice = form.cleaned_data['time']
            services_ids = form.cleaned_data['services']

            time = datetime.strptime(time_choice, '%H:%M').time()
            reserved_time = datetime.combine(date, time)

            services = PetService.objects.filter(pk__in=services_ids)

            subject = 'Reservation Confirmation'
            message = f'Hello {name},\n\nYour reservation has been confirmed.' \
                      f'\n\nReservation Details:\nDate: {date}\nTime: {time_choice}' \
                      f'\nServices: {", ".join(str(service) for service in services)}' \
                      f'\n\nThank you for using our service!' \
                      f'\n\nBest regards,\nThe Reservation Team'
            send_mail(subject, message, 'your_default_from_email', [email])

            reservation = Reservation.objects.create(user=request.user, reserved_time=reserved_time)
            reservation.services.set(services)

            user_profile.desired_service.set(services)

            return redirect(reverse_lazy('home:reservation_success'))
    else:
        form = ReservationForm()

    return render(request, 'reservetime.html', {'form': form})


def reservation_success(request):
    reservation = Reservation.objects.filter(user=request.user).order_by('-id').first()
    return render(request, 'reservation_success.html', {'reservation': reservation})


def about_us(request):
    about_contents = AboutContent.objects.all()
    return render(request, 'about.html', {'about_contents': about_contents})
