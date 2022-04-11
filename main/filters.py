import django_filters
from .models import NewAd


class CarFilter(django_filters.FilterSet):

    car_name_choices = [('Audi', 'Audi'), ('BMW', 'BMW'),
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
                    ('Ужгород', 'Ужгород'), ('Харків', 'Харків'), ('Херсон', 'Херсон'),
                    ('Хмельницький', 'Хмельницький'),
                    ('Черкаси', 'Черкаси'), ('Чернівці', 'Чернівці'), ('Чернігів', 'Чернігів')]

    car_name = django_filters.ChoiceFilter(label='Назва машини', choices=car_name_choices)
    city = django_filters.ChoiceFilter(label='Місто продажу', choices=city_choices)
    year = django_filters.RangeFilter()
    price = django_filters.RangeFilter()

    class Meta:
        model = NewAd
        fields = {
            'car_name',
            'city',
            'year',
            'price'
        }
