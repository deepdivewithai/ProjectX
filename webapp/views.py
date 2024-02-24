import django
from django.shortcuts import render, redirect
from .forms import *

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from .models import Record

from django.contrib import messages

# Homepage

def landing_page(request):
    return render(request, "webapp/index.html")

# Register

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Account created successfully!")

            return redirect("webapp:login")
    
    context = {
        'form': form,
    }
    
    return render(request, "webapp/register.html", context)

# Login

def my_login(request):
    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                messages.success(request, "You are Logged In!")


                return redirect("webapp:dashboard")
            

    context = {
        'form': form,
    }

    return render(request, "webapp/my-login.html", context)


# Dashboard

@login_required(login_url="webapp:login")
def dashboard(request):

    records = Record.objects.all()

    context = {
        "records": records,
    }

    return render(request, "webapp/dashboard.html", context)
    
# Logout

def user_logout(request):
    logout(request)

    messages.success(request, "You are Logged out! 👋👋👋")


    return redirect("webapp:login")



# Read / View a singular Record
@login_required(login_url="webapp:login")
def view_record(request,pk):
    record = Record.objects.get(id=pk)
    context = {'record': record}

    return render(request, "webapp/view-record.html", context)



# Create a record

@login_required(login_url="webapp:login")
def create_record(request):
    form = CreateRecordForm()

    if request.method == "POST":
        form = CreateRecordForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Your record was created!")

            return redirect("webapp:dashboard")
        
    context = {
        'form': form
    }

    return render(request, "webapp/create.html", context)

# Update a record

@login_required(login_url="webapp:login")
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)

    if request.method == "POST":
        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():
            form.save()

            messages.success(request, "Your record was updated!")


            return redirect("webapp:dashboard")
        
    context = {
        'form': form
    }

    return render(request, "webapp/update.html", context)

# Delete a record

@login_required(login_url="webapp:login")
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()

    messages.success(request, "Your record was deleted!")


    return redirect("webapp:dashboard")


