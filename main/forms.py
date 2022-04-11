from django import forms
from django.contrib.auth.models import User
from django.forms import TextInput, Textarea, FileInput, HiddenInput, ChoiceField, Select
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
        car_name_choices = [('Не вказано', 'Виберіть марку автомобіля'), ('Audi', 'Audi'), ('BMW', 'BMW'),
                            ('Chevrolet', 'Chevrolet'), ('Ford', 'Ford'),
                            ('Honda', 'Honda'), ('Hyundai', 'Hyundai'),
                            ('Kia', 'Kia'), ('Lincoln', 'Lincoln'), ('Lexus', 'Lexus'), ('Mazda', 'Mazda'),
                            ('Mercedes-Benz', 'Mercedes-Benz'), ('Mitsubishi', 'Mitsubishi'), ('Nissan', 'Nissan'),
                            ('Opel', 'Opel'), ('Peugeot', 'Peugeot'), ('Renault', 'Renault'), ('Skoda', 'Skoda'),
                            ('Toyota', 'Toyota'), ('Volkswagen', 'Volkswagen'),
                            ('ВАЗ', 'ВАЗ')]

        city_choices = [('Не вказано', 'Виберіть ваш регіон'), ('Київ', 'Київ'), ('Вінниця', 'Вінниця'),
                        ('Дніпро', 'Дніпро'), ('Донецька обл.', 'Донецька обл.'), ('Житомир', 'Житомир'),
                        ('Запоріжжя', 'Запоріжжя'),
                        ('Івано-Франківськ', 'Івано-Франківськ'), ('Кропивницький', 'Кропивницький'),
                        ('Луганська обл.', 'Луганська обл.'), ('Луцьк', 'Луцьк'), ('Львів', 'Львів'),
                        ('Миколаїв', 'Миколаїв'), ('Одеса', 'Одеса'), ('Полтава', 'Полтава'), ('Рівне', 'Рівне'),
                        ('Суми', 'Суми'), ('Тернопіль', 'Тернопіль'),
                        ('Ужгород', 'Ужгород'), ('Харків', 'Харків'), ('Херсон', 'Херсон'), ('Хмельницький', 'Хмельницький'),
                        ('Черкаси', 'Черкаси'), ('Чернівці', 'Чернівці'), ('Чернігів', 'Чернігів')]

        model = NewAd
        fields = ['car_name', 'car_model', 'describe', 'img', 'year', 'price', 'city', 'mileage', 'volume',
                  'drive', 'color', 'transmission', 'number_of_phone']

        widgets = {
            'car_name': Select(attrs={
                'class': 'custom-select',
                'placeholder': 'Введіть назву автомобіля',

            },
                choices=car_name_choices),
            'car_model': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть назву моделі автомобіля',
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
            'city': Select(attrs={
                'class': 'custom-select'
            },
            choices=city_choices),
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
            'drive': Select(
                attrs={'class': 'custom-select'},
                choices=(('Не вказано', 'Виберіть тип приводу'), (2, "Повний"), (3, "Передній"), (4, "Задній"))),

            'color': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введіть колір",
                'style': 'width: 50%; margin-left: 10%; margin-top: 15px'
            }),

            'transmission': Select(
                attrs={'class': 'custom-select'},
                choices=(('Не вказано', 'Виберіть тип коробки передач'), ("Ручна", "Ручна"), ("Автомат", "Автомат"))),

            'number_of_phone': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Введіть Ваш номер телефону",
                'style': 'width: 50%; margin-left: 10%; margin-top: 15px'
            }),
        }
