from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import RequestContext
import pymysql
from datetime import date
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
import random
#database Connection
from django.db import connection

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request, "about.html")

def team(request):
    return render(request, "team.html")

def registration(request):
    return render(request, 'registration.html')

def Reg(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        
        with connection.cursor() as cursor:
            sql = "INSERT INTO registration(name,email,contact,password) VALUES (%s,%s,%s,%s)"
            values = (name, email, contact, password)
            cursor.execute(sql, values)
        
        return render(request, "login.html") 

def login(request):
    return render(request, "login.html")

def dologin(request):
    user_email = request.POST.get('email')
    passw = request.POST.get('password')
    
    with connection.cursor() as cursor:
        sql = "SELECT id, name, email, contact, password FROM registration"
        cursor.execute(sql)
        rows = cursor.fetchall()
   
    ispresent = False
    id = ""
    for x in rows:
        # x indexes: 0:id, 1:name, 2:email, 3:contact, 4:password
        if user_email == x[2] and passw == x[4]:
            name = x[1]
            id = x[0]
            ispresent = True
            break
            
    if ispresent:
        request.session['id'] = id
        return render(request, "dashboard.html")
    else:
        return render(request, "invalid.html")


def AdminDashboard(request):
    return render(request, "AdminDashboard.html")

def AdminLogin(request):
    if request.method == 'POST':
        username = request.POST.get('text')  # Changed from 'username' to 'text'
        password = request.POST.get('password')

        if username == "admin" and password == "admin":
            return render(request, "AdminDashboard.html")  # Add .html extension
        else:
            # Handle incorrect login attempt
            return render(request, "AdminLogin.html", {'error': 'Invalid username or password.'})  # Adjust as needed
    else:
        # For GET requests, render the admin login template
        return render(request, "AdminLogin.html")  # Adjust as needed

def Add_Food(request):
    return render(request, "Add_Food.html")
