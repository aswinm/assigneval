from django.shortcuts import render
from users.models import MyUser
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from users.forms import RegisterForm,LoginForm

def index(request):
    return render(request,"index.html")

@login_required(login_url="/login")
def logoff(request):
    logout(request)
    return HttpResponseRedirect("/")

def register(request):
    d = {}
    d["url"] = "/register"
    d["sub"] = "Register"
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            u = form.save(commit = False)
            password = form.cleaned_data["password"]
            u.set_password(password)
            u.save()
            return HttpResponseRedirect("/")
        else:
            d["form"] =form
            return render(request,"register.html",d)

    else:
        d["form"] = RegisterForm()
        return render(request,"register.html",d)


def logon(request):
    d = {}
    d["url"] = "/login"
    d["sub"] = "Login"
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect("/")
            else:
                d["form"] = form
                d["text"] = "Invalid login credentials"
                return render(request,"register.html",d)


        else:
            d["form"] = form
            return render(request,"register.html",d)

    else:
        d["form"] = LoginForm()
        return render(request,"register.html",d)
# Create your views here.
