from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import CreateNewGoal

import sys
sys.path.append("..")
from SQL.sql_connector import *

from home import modules # Create goal class and add it to html

connector = Connector('project')

# Create your views here.
def index(request, user):
    # if he logged in
    if user != "default":
        user_id = connector.get_data('users', 'id', 'username', user)[0][0]
        # if he submitted a form
        if request.method == "POST":
            form = CreateNewGoal(request.POST)   
            if form.is_valid():
                goal = form.cleaned_data["goal"]
                deadline = form.cleaned_data["deadline"]
                # add to goal table
                connector.add_data('goals', ('user_id', 'goal', 'deadline', 'stts'), (user_id, goal, deadline, "not_done"))
        
        goal_list = connector.get_data('goals', column="user_id", values=str(user_id))
        week_list = []
        for goal in goal_list:
            week_list.append(modules.Goal(goal[2], goal[3], goal[4]))

        form = CreateNewGoal()
        
        return render(request, 'home/index.html', {
            "form": form,
            "username": user,
            "week_list": week_list
        })
    else:
        return render(request, 'home/index.html')

def login(request):
    if request.method == "POST":
        # Check if credentials are there
        usernames = connector.get_data('users', 'username')[0]
        for username in usernames:
            if request.POST['username'] == username:
                user_exists = True
                break
            else:
                user_exists = False
        if user_exists:
            password = connector.get_data('users', 'password', 'username', username)[0][0]
            if password == request.POST['password']:
                return redirect(reverse('home:index', kwargs={'user':username}))
            else:
                return render(request, 'home/login.html',{
                    "error" : "Credential Incorrect"
                })
        else:
            return render(request, 'home/login.html', {
                "error": "Credentials Incorrect"
            })
    else:
        return render(request, 'home/login.html')

def register(request):    
    if request.method == "POST":
        #Check if username taken
        usernames = connector.get_data('users', 'username')[0]
        for username in usernames:
            if username == request.POST["username"]:
                return render(request, "home/register.html",{
                    "error": "Username already taken"
                })
        # Check if two passwords are the same 
        if request.POST["password1"] == request.POST["password2"]:
            credentials = [request.POST["username"], request.POST["password1"]]            
            connector.add_data("users", ('username', 'password'), (credentials[0], credentials[1]))
            return redirect(reverse('home:index', kwargs={'user':credentials[0]}))
        else:
            return render(request, 'home/register.html', {
                "error": "Your two passwords aren't the same"
            })        
    else:
        return render(request, 'home/register.html')
