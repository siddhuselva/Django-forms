from django import forms

class sinform(forms.Form):
    uname1 = forms.CharField(max_length=30)
    upswd1 = forms.CharField(max_length=8,widgets = forms.PasswordInput())

class upform(forms.Form):
    uname2 = forms.CharField(max_length=30)
    uemail2 = forms.EmailField(max_length=50)
    upswd2 = forms.CharField(max_length=8)
