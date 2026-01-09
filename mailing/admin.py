from django.contrib import admin

from .models import Recipient, Message, Mailing, AttemptLog


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "name", "comment")
    list_filter = ("email", "name", "comment",)
    search_fields = (
        "email",
        "name",
        "comment",
    )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "subject", "body")
    list_filter = ("subject", "body",)
    search_fields = (
        "subject",
        "body",
    )


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ("id", "start_time", "end_time", "message", "status")
    list_filter = ("start_time", "end_time", "message", "status",)
    search_fields = (
        "start_time",
        "end_time",
        "message",
        "status",
    )


@admin.register(AttemptLog)
class AttemptLogAdmin(admin.ModelAdmin):
    list_display = ("id", "attempt_time", "status", "server_response", "mailing")
    list_filter = ("attempt_time", "status", "server_response", "mailing",)
    search_fields = (
        "attempt_time",
        "status",
        "server_response",
        "mailing",
    )
