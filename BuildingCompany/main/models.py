from django.db import models


class BuildingCompany(models.Model):
    company_name = models.CharField(max_length=255, verbose_name='Название компании')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Email')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.company_name


class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название услуги')
    image = models.ImageField(upload_to='services/', verbose_name='Фото услуги')

    def __str__(self):
        return self.name
