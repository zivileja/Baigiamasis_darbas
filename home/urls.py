from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'home'
urlpatterns = [

    path("signup/", views.SignUpView.as_view(), name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("services/", views.services, name="services"),
    path('profile/', views.profile, name='profile'),
    path('add_pet_service/', views.add_pet_service, name='add_pet_service'),
    path("reservetime/", views.reservetime, name="reservetime"),
    path('reservation_success/', views.reservation_success, name='reservation_success'),
    path('', views.home, name="home"),

]
