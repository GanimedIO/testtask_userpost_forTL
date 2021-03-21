from django.db import models

# Create your models here.

class Posts(models.Model):
	userId = models.ForeignKey('Users', on_delete=models.DO_NOTHING, null=True)
	title = models.CharField(max_length=100)
	body = models.CharField(max_length=200)

class Geo(models.Model):
	lat = models.CharField(max_length=100)
	lng = models.CharField(max_length=100)

class Address(models.Model):
	street = models.CharField(max_length=100)
	suite = models.CharField(max_length=100)
	city = models.CharField(max_length=100)
	zipcode = models.CharField(max_length=100)
	geo = models.ForeignKey('Geo', on_delete=models.CASCADE, null=True)
	#geo = models.ManyToManyField(Geo)

class Company(models.Model):
	name = models.CharField(max_length=100)
	catchPhrase = models.CharField(max_length=100)
	bs = models.CharField(max_length=100)

class Users(models.Model):
	name = models.CharField(max_length=100)
	username = models.CharField(max_length=100)
	email= models.CharField(max_length=100)
	address = models.ForeignKey('Address', on_delete=models.CASCADE, null=True)
	phone = models.CharField(max_length=100)
	website = models.CharField(max_length=100)
	company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True)
	#company = models.ManyToManyField(Company)