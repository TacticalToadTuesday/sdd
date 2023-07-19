from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from login import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from . tokens import generate_token
from django.core.mail import EmailMessage, send_mail
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
import openai
import json
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from .models import Response

# Renders the home page
def home(request):
    return render(request, "authentication/index.html")

# Renders the dashboard page, accessible only to logged-in users
@login_required
def dashboard(request):
    first_name = request.user.first_name
    return render(request, "authentication/dashboard.html", {'first_name': first_name})

# Handles the signup functionality
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('signup')

        # Check if the email is already registered
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('signup')

        # Validate the length of the username
        if len(username) > 15:
            messages.error(request, "Username must be under 15 characters.")
            return redirect('signup')

        # Validate the length of the username
        if len(username) == 0:
            messages.error(request, "Username must be at least one character.")
            return redirect('signup')

        # Validate the length of the email
        if len(email) == 0:
            messages.error(request, "Email must be at least one character.")
            return redirect('signup')

        # Validate the length of the firstname
        if len(firstname) == 0:
            messages.error(request, "First name must be at least one character.")
            return redirect('signup')

        # Validate the length of the lastname
        if len(lastname) == 0:
            messages.error(request, "Last name must be at least one character.")
            return redirect('signup')

        # Validate the length of the password
        if len(password) == 0:
            messages.error(request, "Password must be at least one character.")
            return redirect('signup')

        # Validate that the username is alphanumeric
        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric.")
            return redirect('signup')

        # Create a new user account
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()

        messages.success(request, "Account created successfully. Please sign in.")
        return redirect('signin')

    # Renders the signup page
    return render(request, 'authentication/signup.html')


# Handles the signin functionality
def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user is not None:
            # Login the user
            login(request, user)
            firstname = user.first_name
            return redirect('dashboard')

        else:
            messages.error(request, "Either your username or password is incorrect.")

    # Renders the signin page
    return render(request, "authentication/signin.html")

# Handles the signout functionality
def signout(request):
    # Logout the user
    logout(request)
    return redirect('home')



    


@login_required
def submit_form_view(request):
    if request.method == 'POST':
        
        # Get form data from the request
        studentclass = request.POST.get('class')
        student = request.POST.get('student')
        behaviour = int(request.POST.get('behaviour'))
        attendance = int(request.POST.get('attendance'))
        grades = int(request.POST.get('grades'))

        def get_description(category, number):
            # Helper function to get the description based on category and number
            if category == "Behavior":
                if number == 1:
                    return "Disruptive"
                elif number == 2:
                    return "Inattentive"
                elif number == 3:
                    return "Inconsistent"
                elif number == 4:
                    return "Passive"
                elif number == 5:
                    return "Cooperative"
                elif number == 6:
                    return "Engaged"
                elif number == 7:
                    return "Exemplary"
            elif category == "Attendance":
                if number == 1:
                    return "Absentee"
                elif number == 2:
                    return "Irregular"
                elif number == 3:
                    return "Sporadic"
                elif number == 4:
                    return "Tardy"
                elif number == 5:
                    return "Adequate"
                elif number == 6:
                    return "Punctual"
                elif number == 7:
                    return "Exceptional"
            elif category == "Grades":
                if number == 1:
                    return "Failing"
                elif number == 2:
                    return "Poor"
                elif number == 3:
                    return "Mediocre"
                elif number == 4:
                    return "Average"
                elif number == 5:
                    return "Satisfactory"
                elif number == 6:
                    return "Good"
                elif number == 7:
                    return "Excellent"

        # Get the actual descriptions based on form data
        behaviourActual = str(get_description("Behavior", behaviour))
        attendanceActual = str(get_description("Attendance", attendance))
        gradesActual = str(get_description("Grades", grades))

        print(behaviourActual)
        print(attendanceActual)
        print(gradesActual)

        # Make an API request to generate the student report
        openai.api_key = "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"
        #pls dont steal

        prompt = f"Write a student report to go on a report card for their parents from the perspective of their {studentclass} teacher who knows their students well in {studentclass} with name {student}, whose attendance is {attendanceActual}, their grades are {gradesActual}, and their behavior is {behaviourActual}. Ensure it all flows nicely with no line breaks or titles before sections. Write one sentence on each of the three areas every time. Hard maximum is 120 words. DO NOT EXCEED"
        response = str(openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                "role": "user",
                "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=232,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
            ))
        
        parsed_data = json.loads(response)
        content = parsed_data['choices'][0]['message']['content']

        print(content)
        
        # Store the result in the database for the authenticated user (DEPRECATED)
        # user = request.user  # Assuming you have authentication set up
        # Response.objects.create(user=user, result=result_text)
        
        context = {'result': content}
        return render(request, 'authentication/dashboard.html', context)

    # Render the dashboard page
    return render(request, 'authentication/dashboard.html')


@login_required
def config(request):
    # Retrieve the first name of the logged-in user
    first_name = request.user.first_name
    return render(request, 'authentication/config.html')

def help(request):
    # render template correctly
    return render(request, 'authentication/help.html')
