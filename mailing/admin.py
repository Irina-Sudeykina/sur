from django.contrib import admin

from .models import Recipient


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "name", "comment")
    list_filter = ("email", "name", "comment",)
    search_fields = (
        "email",
        "name",
        "comment",
    )
