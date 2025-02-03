from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse

# User Registration
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect("dashboard")  # Redirect to the dashboard
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})

# User Login
def custom_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")  # Redirect to dashboard
        else:
            return render(request, "users/login.html", {"error": "Invalid username or password"})
    return render(request, "users/login.html")

# User Logout
def custom_logout(request):
    logout(request)
    return redirect("login")  # Redirect to login page after logout







# from django.shortcuts import render
# from django.contrib.auth import authenticate, login
# from django.http import HttpResponseRedirect

# def custom_login(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect("/dashboard/")  # Redirect to the dashboard after login
#         else:
#             return render(request, "users/login.html", {"error": "Invalid username or password"})
#     return render(request, "users/login.html")

