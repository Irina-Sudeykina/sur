from django.urls import path

from mailing.apps import MailingConfig
from mailing.views import (RecipientListView, RecipientDetailView, RecipientCreateView, RecipientUpdateView,
    RecipientDeleteView)

app_name = MailingConfig.name

urlpatterns = [
    path("", RecipientListView.as_view(), name="recipient_list"),
    path("recipient/<int:pk>/", RecipientDetailView.as_view(), name="recipient_detail"),
    path("recipient/create/", RecipientCreateView.as_view(), name="recipient_create"),
    path("recipient/<int:pk>/update/", RecipientUpdateView.as_view(), name="recipient_update"),
    path("recipient/<int:pk>/delete/", RecipientDeleteView.as_view(), name="recipient_delete"),
    # path("category", CategoryListView.as_view(), name="category_list"),
    # path("category/<int:pk>/", CategoryDetailView.as_view(), name="category_detail"),
]
