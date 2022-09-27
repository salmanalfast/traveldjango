from django.db import models

# Create your modelsmodels.Model
class foodmenu(models.Model):
	foods = models.CharField(max_length=255)
	price = models.CharField(max_length=255)

class drinkmenu(models.Model):
	drinks = models.CharField(max_length=255)
	price = models.CharField(max_length=255)

class users(models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	password = models.CharField(max_length=255)

class imagedb(models.Model):
  	images = models.BinaryField()
		