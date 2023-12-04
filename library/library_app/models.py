from django.db import models
# from django.contrib.auth.models import User


class Book(models.Model):
	book = models.CharField(max_length = 200, blank=True, null=True)

	def __str__(self):
		return self.book

class Student(models.Model):
	name = models.CharField(max_length = 200, blank=True, null=True)
	book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
	

	def __str__(self):
		return self.name

# class Like(models.Model):
# 	# user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	# book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)

# 	def __str__(self):
# 		# return f"{self.user.username} - {self.book}"
# 		retun f"{self}"
