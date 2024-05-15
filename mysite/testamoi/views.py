from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import RegisterForm 
from django.db import connection

from http import cookies
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.shortcuts import render
import mysql.connector


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# db = mysql.connector.connect (  
#     "NAME": "db",
#     "USER": "root",
# "PASSWORD": "password",
# "HOST": "127.0.0.1"
# )
       
    



class Home(APIView):
    
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)
    
def createAndReadCookies(request):

        response = render(request,'Index.html')

        response.set_cookie(key="user_id",value="M-user_id",secure=True,)
        user_id = request.COOKIES.get('user_id')

        if user_id:
                    return HttpResponse (f"welcom {user_id}")
        else:
                    return HttpResponse("welcom new user ")


    

def singnup (request):
    
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaner_data.get('username')
            password = form.cleaner_data.get('password')
            user = auth.authenticate(username=username, password=password)

            query = f"INSERT INTO users (username, password, role) VALUES ('{username}', '{password}', 'client');"
            return redirect('Index/')
        if user is not None:
             auth.login(request, user) 
            #user = authenticate(username='username', password='password')
            #Login(request, user)

             return redirect('error')
        else:
            return render(request, '' ,{'form':form})
        
    else:
        form = UserCreationForm()
        return render(request, 'singup.html')

def Index(request):

    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'GET' :
        return render(request, 'Index.html', context={'form' : RegisterForm})
   
    else:
        form = UserCreationForm()
        return render(request, 'Index.html') 


def Order(request): 
    return render(request, 'Order.html')
    # query = f"INSERT INTO Order (user_id, product_id, created_at,total) VALUES ('{}', '{product}', 'client');" 

def Product(request):
    return render(request, 'Product.html')


def Registration(request):

    print(request.method)

    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)

    if request.method == 'GET':
        return render(request, 'Login.html', context={'form' : RegisterForm})
    
    elif request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # requete base de données
            query = f"INSERT INTO users (username, password, role) VALUES ('{username}', '{password}', 'client');"



            print(username)
            print(password)
            print(query)
            my_custom_sql(query)
            

def Shop(request):
    
    return render(request, 'Shop.html')


def Login(request):

    if request.method == 'GET':
        return render(request, 'Login.html', context={'form' : RegisterForm})
   
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
           
            
            with connection.cursor() as cursor:
                    # cursor.execute("INSERT INTO users (username, password, role) VALUES (%s, %s, 'client')", [username, password])
                    sql= f"SELECT * users where username = ${username} and password = ${password});"
            return render(request, 'Index.html')
        else: 
            return render(request, 'Login.html')
        
# def my_custom_sql(query):
#     with connection.cursor() as cursor:
#         cursor.execute(query)
#         row = cursor.fetchone()
#     return row

