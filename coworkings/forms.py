from django.contrib.auth.forms import UserCreationForm
from django import forms

from coworkings.models import User


class CustomUserCreationForm(UserCreationForm):
    fullname = forms.CharField(
        label='Имя и фамилия',
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Иван Иванов'})
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'ваш@email.com'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'fullname', 'email', 'password1', 'password2')

    def clean_password2(self):
        pass1 = self.cleaned_data.get("password1")
        pass2 = self.cleaned_data.get("password2")
        if pass1 and pass2 and pass1 != pass2:
            raise forms.ValidationError('Пароли не совпадают')
        return pass2


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