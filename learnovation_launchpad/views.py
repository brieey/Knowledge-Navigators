from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ContactForm
from django.contrib import messages  
from django.contrib.auth import login, authenticate 
from .forms import SignUpForm 
# This file renders all of the templates 

def home(request):
    return render(request, 'index.html')
    

def about(request):
    return render(request, 'about.html') 


def contact(request):
    #Checks if the form was submitted
    if request.method == 'POST':
        firstName = request.POST.get('firstName').strip()
        lastName = request.POST.get('lastName').strip()
        email = request.POST.get('email').strip()
        phoneNumber = request.POST.get('phoneNumber').strip()
        message = request.POST.get('message').strip()

        #Create the instance
        new_form = ContactForm(firstName=firstName, lastName=lastName, email=email, phoneNumber=phoneNumber, message=message)

        #Save the instance
        new_form.save()

        # Let's the user know the form has been submitted
        messages.success(request, 'Message sent successfully!')

        #Redirects the user to the same page
        return redirect('contact')

    #Render the contact page with the form
    return render(request, 'contact.html') 

        

def login(request):
    return render(request, 'login.html') #This renders login template
    

def signup(request):
    print("Signup view called")
    if request.method == 'POST':
        form = SignUpForm(request.POST) 
        if form.is_valid(): 
            print("form is valid")
            form.save() 
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1') 
            new_user = authenticate(email=email, password=password)
            if new_user is not None: 
                login(request, new_user) 
                return redirect('home') 
            else:
                print("authentication failed")
        else:
            print("form is invalid")
            print(form.errors)
    form = SignUpForm()
    context = {  'form': form  } 
    return render(request, 'signup.html', context) #This renders the signup template

def profile(request):
    return render(request, 'profile.html') #This renders the profile template
    
