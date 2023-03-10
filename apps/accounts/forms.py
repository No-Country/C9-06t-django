from django.forms import ModelForm, TextInput, EmailInput
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

from .models import UserProfile


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        # exclude = ['user']


class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control form-control-md', 'type': 'password', 'align': 'center'}))
    password2 = forms.CharField(label="Confirm password",
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control form-control-md', 'type': 'password', 'align': 'center'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'username': TextInput(attrs={
                'class': "form-control form-control-md",}),
            'first_name': TextInput(attrs={
                'class': "form-control form-control-md"}),
            'last_name': TextInput(attrs={
                'class': "form-control form-control-md"}),
            'email': EmailInput(attrs={
                'class': "form-control form-control-md"}),
        }


class UserEditForm(UserChangeForm):

    password = forms.CharField(
    help_text="",
    widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['email','first_name','last_name']

    #Verificacion

    def clean_password2(self):
        
        password2 = self.cleaned_data["password2"]
        password1 = self.cleaned_data["password1"]

        if password2 != password1:
            raise forms.ValidationError("Las contraseñas no coinciden!")
        
        return password2
    
