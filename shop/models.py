from django.db import models


class Product(models.Model):
	name = models.CharField('Название', max_length=100)
	description = models.CharField('Описание', max_length=200)
	price = models.CharField('Цена', max_length=100)
	date = models.DateTimeField('Дата')

	def __str__(self):
		return self.name