from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'country', 'region', 'city')
        
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['email']  # Set username to email
        if commit:
            user.save()
        return user

class CustomUserChangeForm(forms.ModelForm):
    email = forms.EmailField(disabled=True)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone_number', 'country', 'region', 'city', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['readonly'] = True

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('profile_picture',)