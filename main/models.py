from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='название')
    price = models.CharField(max_length=10, verbose_name='Цена')
    weight = models.FloatField(max_length=20, verbose_name='Вес')
    term = models.DateTimeField(verbose_name='Срок изготовления')
    image = models.ImageField(upload_to='img/%Y/%m/%d', blank=True)
    compound = models.CharField(max_length=30, verbose_name='Состав')

    def __str__(self):
        return f"{self.name} - {self.image}"


class Employee(models.Model):
    name = models.CharField(max_length=50, verbose_name='имя')
    first_name = models.CharField(max_length=50)
    availability = models.BooleanField(default=True, verbose_name='azyrky uchurda ishteyt')
    image = models.ImageField(upload_to='p/%Y/%m/%d', blank=True)
    position = models.CharField(max_length=50)
    email = models.EmailField()
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание')
    website = models.URLField(max_length=200, blank=True, null=True, verbose_name='Ссылка на сайт')

    def __str__(self):
        return f"{self.name} - {self.image}"
