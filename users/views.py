from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from . import models
from . import forms


def profiles(request):
    users_profiles = models.Profile.objects.all()
    context = {
        "profiles": users_profiles
    }
    return render(request, "users/profiles.html", context)


def profile(request, pk):
    user_profile = models.Profile.objects.get(id=pk)

    top_skills = user_profile.skill_set.exclude(description__exact="")
    other_skills = user_profile.skill_set.filter(description="")

    context = {
        "profile": user_profile,
        "top_skills": top_skills,
        "other_skills": other_skills
    }
    return render(request, "users/profile.html", context)


@login_required(login_url="login")
def account(request):
    user_profile = request.user.profile
    context = {
        "profile": user_profile
    }
    return render(request, "users/account.html", context)


@login_required(login_url="login")
def account_edit(request):
    user_profile = request.user.profile
    form = forms.ProfileEdirForm(instance=user_profile)

    if request.method == "POST":
        form = forms.ProfileEdirForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "O'zgarishlar muvaffaqiyatli saqlandi !")
            return redirect("account")
        else:
            messages.error(request, "Forma notog'ri to'ldirilgan !")

    context = {
        "form": form
    }
    return render(request, "users/profile_edit.html", context)


def user_register(request):
    form = forms.UserRegistrationForm()
    if request.method == "POST":
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            messages.success(request, f"Akkaunt muvaffaqiyatli yaratildi. Assalomu alaykum {user.profile.full_name} !")
            return redirect("account")
        else:
            messages.error(request, "Form filled incorrectly !")
            return redirect("register")

    context = {
        "form": form,
        "page": "register"
    }
    return render(request, "users/login_register.html", context)


def user_login(request):
    if request.user.is_authenticated:
        messages.error(request, "Logout first to login !")
        return redirect("profiles")
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            messages.success(request, f"Xush kelibsiz {user.profile.full_name} !")
            return redirect("profiles")
        else:
            messages.error(request, "Username yoki Parol xato !")
    context = {
        "page": "login"
    }
    return render(request, "users/login_register.html", context)


def user_logout(request):
    logout(request)
    messages.info(request, "Akkauntdan chiqdingiz")
    return redirect("login")
