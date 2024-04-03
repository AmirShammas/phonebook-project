from django.contrib import admin
from .models import City, Phone


class CityAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_active", "created_at")


class PhoneAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "first_name", "last_name",
                    "mobile", "city", "is_active",)


admin.site.register(City, CityAdmin)

admin.site.register(Phone, PhoneAdmin)
