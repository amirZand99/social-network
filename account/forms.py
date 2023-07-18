from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile


class UserRegisterationForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(widget= forms.EmailInput(attrs={'placeholder':'your email'}))
    password1 = forms.CharField(label='password', widget = forms.PasswordInput(attrs = {'placeholder':'your password'}))
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(attrs={'placeholder': 'your password'}))

    #def clean_email(self):
       # email= self.cleaned_data['email']
       # user = User.objects.filter(email=email).exists
     #   if user:
         #    raise ValidationError('this email already exists.')

       # return email


    def clean(self):
        cd= super().clean()
        p1= cd.get('password1')
        p2= cd.get('password2')
        if p1 and p2 and p1 != p2:
            raise ValidationError('password must match.')


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'your password'}))


class EditUserForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = Profile
        fields = ('age', 'bio')
