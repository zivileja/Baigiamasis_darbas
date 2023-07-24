from django.contrib import admin
from .models import AboutContent, PetService, Reservation, Profile


class AboutContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


class PetServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'reserved_time', 'get_services_names')

    def get_services_names(self, obj):
        return ", ".join(str(service) for service in obj.services.all())

    get_services_names.short_description = 'Desired Services'



class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'get_preferred_services')

    def get_preferred_services(self, obj):
        return ", ".join(str(service) for service in obj.desired_service.all())

    get_preferred_services.short_description = 'Desired Services'


admin.site.register(AboutContent, AboutContentAdmin)
admin.site.register(PetService, PetServiceAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Profile, ProfileAdmin)
