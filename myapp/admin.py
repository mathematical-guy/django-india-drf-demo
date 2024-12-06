from django.contrib import admin

from myapp.models import Wizard


@admin.register(Wizard)
class WizardAdmin(admin.ModelAdmin):
    list_display = ("name",)

    ordering = ("created_at",)