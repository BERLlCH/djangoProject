# Generated by Django 4.0.1 on 2022-01-15 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newad',
            name='number_of_phone',
            field=models.CharField(default=523, max_length=10, verbose_name='Номер телефона'),
            preserve_default=False,
        ),
    ]
