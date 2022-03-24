from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, Textarea, FileInput, HiddenInput
from .models import NewAd


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторить пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class NewAdForm(forms.ModelForm):
    class Meta:
        model = NewAd
        fields = ['car_name', 'describe', 'img','user_id', 'year', 'price', 'city', 'mileage', 'volume',
                  'drive', 'color', 'transmission', 'number_of_phone']

        widgets = {'car_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть назву автомобіля',
                'style': 'width: 50%; margin-left: 10%; margin-top: 15px'
            }),
            'describe': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть опис для автомобіля',
                'style': 'width: 50%; margin-left: 10%; margin-top: 15px; height: 100px'
            }),
            'img': FileInput(attrs={
                'class': 'form-control',
                'style': 'width: 50%; margin-top: 15px; margin-left: 10%'
            }),
            'year': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть рік випуску',
                'style': 'width: 50%; margin-left: 10%; margin-top: 15px'
            }),
            'price': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть вартість машини(в $)',
                'style': 'width: 50%; margin-left: 10%; margin-top: 15px'
            }),
            'city': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть місто продажу',
                'style': 'width: 50%; margin-left: 10%; margin-top: 15px'
            }),
            'mileage': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть пробіг(в тис. км.)',
                'style': 'width: 50%; margin-left: 10%; margin-top: 15px'
            }),
            'volume': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введіть об'єм двигуна та тип палива",
                'style': 'width: 50%; margin-left: 10%; margin-top: 15px'
            }),
            'drive': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введіть тип приводу",
                'style': 'width: 50%; margin-left: 10%; margin-top: 15px'
            }),
            'color': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введіть колір",
                'style': 'width: 50%; margin-left: 10%; margin-top: 15px'
            }),
            'transmission': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введіть тип трансмісії",
                'style': 'width: 50%; margin-left: 10%; margin-top: 15px'
            }),
            'number_of_phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введіть Ваш номер телефону",
                'style': 'width: 50%; margin-left: 10%; margin-top: 15px'
            }),
            'user_id': HiddenInput(attrs={
                'value': 1
            })
        }
