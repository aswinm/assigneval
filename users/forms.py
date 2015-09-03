from django import forms
from users.models import MyUser

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=100,widget=forms.PasswordInput())
    class Meta:
        model = MyUser
        fields = ('username','first_name','last_name','email','is_staff','designation','password')
        widgets = {
                'password':forms.PasswordInput()
                }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=100,widget=forms.PasswordInput())
