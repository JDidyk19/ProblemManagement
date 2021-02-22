from django import forms
from django.contrib.auth import password_validation
from .models import UserProfile

class UserLoginForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['username', 'password']

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not UserProfile.objects.filter(username=username).exists():
            raise forms.ValidationError(f'користувач з логіном "{username} не найдено в системі')

        user = UserProfile.objects.filter(username=username).first()
        if user:
            if not user.check_password(password):
                raise forms.ValidationError("Невірний пароль")
        return self.cleaned_data

class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserProfile.objects.filter(email=email).exists():
            raise forms.ValidationError(
                f'Дана поштова адреса вже зареєстрована в системі'
            )
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if UserProfile.objects.filter(username=username).exists():
            raise forms.ValidationError(
                f'Ім\'я {username} зайнято'
            )
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password')
        # if forms.ValidationError:
        #     raise forms.ValidationError(f'{password} is bad')
        # return password
        try:
            password_validation.validate_password(password, self.instance)
        except forms.ValidationError as error:
            self.add_error('password', error)
        return password

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password']