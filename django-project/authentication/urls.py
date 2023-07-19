from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),  # URL pattern for the home page
    path('home', views.home, name="home"),  # URL pattern for the home page
    path('dashboard', views.dashboard, name='dashboard'),  # URL pattern for the dashboard page
    path('signup', views.signup, name="signup"),  # URL pattern for the signup page
    path('signin', views.signin, name="signin"),  # URL pattern for the signin page
    path('signout', views.signout, name="signout"),  # URL pattern for the signout page
    path('config', views.config, name='config'),  # URL pattern for the config page
    path('help', views.help, name='help'),  # URL pattern for the config page
    path('submit-form', views.submit_form_view, name='submit_form'),  # URL pattern for the submit form view
]

