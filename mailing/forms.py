from django import forms
from django.core.exceptions import ValidationError

from .models import Recipient


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs["class"] = "form-check-imput"
            else:
                field.widget.attrs["class"] = "form-control"


class RecipientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Recipient
        exclude = ("owner",)
