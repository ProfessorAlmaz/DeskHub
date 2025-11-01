from django.contrib.auth.forms import UserCreationForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'forms-control'
            field.help_text = None

class UserAuthForm(forms.Form):
    username = forms.CharField(
        label="Имя пользователя",
        widget=forms.TextInput(
            attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        ),
        strip=False
    )

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(username) < 3:
            self.errors['username'] = "Поле не может быть меньше 3 символов"
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            self.errors['password'] = 'Пароль не может быть меньше 8 символов'
        return password