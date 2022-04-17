from django.db import models

# Create your models here.

## create restApi - section 2

class Student(models.Model):


	name = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)

	def __str__(self):

		return self.name + ' - '+ self.phone