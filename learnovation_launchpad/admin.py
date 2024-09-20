from django.contrib import admin #This line imports the admin module
from .models import * #This line imports the ContactForm 


# Register your models here.
admin.site.register(ContactForm)

admin.site.register(SignUp) #This line registers the SignUp model
