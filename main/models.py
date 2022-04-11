from django.db import models


class NewAd(models.Model):
    car_name = models.CharField('Назва машини', max_length=70)
    car_model = models.CharField('Модель машини', max_length=35, blank=True)
    describe = models.TextField('Опис автомобіля', max_length=800)
    img = models.ImageField(    upload_to='media/cars')
    user_id = models.CharField('ID користувача', max_length=10, blank=True)
    user_name = models.CharField('Імя користувача', max_length=10, blank=True)
    year = models.CharField('Рік випуску автомобіля', max_length=4)
    price = models.CharField('Ціна автомобіля', max_length=6)
    city = models.CharField('Місто продажу', max_length=15)
    mileage = models.CharField('Пробіг автомобіля', max_length=7)
    volume = models.CharField("Об'єм двигуна і тип палива", max_length=30)
    drive = models.CharField('Привід автомобіля', max_length=10)
    color = models.CharField('Колір автомобіля', max_length=15)
    transmission = models.CharField('Тип трансмісії', max_length=15)
    number_of_phone = models.CharField('Номер телефона', max_length=10)
