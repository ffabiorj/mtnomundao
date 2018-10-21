from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.core.validators import ValidationError
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from .models import User


class UserAdminCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'name', 'age', 'qnt', 'city', 'email', 'about', 'photo']
        widgets = {
          'about': forms.Textarea(attrs={'rows':5, 'cols':40}),
        }


class UserAdminChangeForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['about', 'email', 'qnt', 'photo']
        widgets = {
          'about': forms.Textarea(attrs={'rows':5, 'cols':40}),
        }

class UserAdminForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'name', 'age', 'qnt', 'city', 'about', 'photo', 'is_active', 'is_staff']
        widgets = {
          'about': forms.Textarea(attrs={'rows':5, 'cols':40}),
        }


class UserPhoto(forms.ModelForm):
    def clean_image(self):
        image = self.cleaned_data.get("photo", False)
        if image:
            if image.__sizeof__ > 5*1024*1024:
                raise ValidationError("Imagem muito grande, tem que ser menor 5mb.")
            return image
        else:
            raise ValidationError("A image não pode se aberta.")