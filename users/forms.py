from django import forms

from .models import User


class CreateAccountForm(forms.ModelForm):
    """Form for creating new accounts."""
    password1=forms.CharField(widget=forms.PasswordInput)
    password2=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','email','password1','password2')

    def clean(self):
        clean_data=super().clean()
        password1=clean_data.get('password1')
        password2=clean_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('passwords don\'t match')
        return clean_data

    def save(self, commit=True):
        user=super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user



class ChangePasswordForm(forms.Form):
    """Form for changing password."""
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    username=forms.CharField(max_length=100)

    def clean(self):
        clean_data = super().clean()
        password1 = clean_data.get('password1')
        password2 = clean_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('passwords don\'t match')
        return clean_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    """Form for login"""
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

