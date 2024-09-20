from django.db import models


#Model created to save submitted contact form data
class ContactForm(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=10)
    message = models.TextField()

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


#Model created to save submitted signup form
class SignUp(models.Model):
    username = models.CharField(max_length=16)
    email = models.EmailField()
    password = models.CharField(max_length=16)

    def __str__(self):
        return f"{self.username} {self.email}"
