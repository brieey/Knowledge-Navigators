from django.urls import path
from . import views

#If you have any specific routes or views you want to add, you can define them in the
# urls.py and the views.py files in the learnovation_launchpad directory.

urlpatterns = [
    path('', views.home, name='home'), #Home Page View
    path('about/', views.about, name='about'), #About Page View
    path('contact/', views.contact, name='contact'), #Contact Page View
    path('login/', views.login, name='login'), #Login Page View
    path('signup/', views.signup, name='signup'), #Login Page View
]