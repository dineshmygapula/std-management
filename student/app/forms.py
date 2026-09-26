from django.forms import ModelForm
from app.models import Company
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = "__all__"

    def clean(self):
        name = self.cleaned_data["name"]
        location = self.cleaned_data["location"]
        if name.lower() == "google" and location.lower() == "mars":
            raise ValidationError("loction cannot be marks ")
        return self.cleaned_data


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean(self):
        username = self.cleaned_data["username"]
        email = self.cleaned_data["email"]
        if username == "dinesh" and email != "dinesh@gmail.com":
            return ValidationError("Dinesh must use dinesh@gmail.com")
        return self.cleaned_data
