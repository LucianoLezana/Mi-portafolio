from django.shortcuts import render


def Home(request):

    return render(request, "WebLucianoApp/home.html")


def About(request):

    return render(request, "WebLucianoApp/about-me.html")


def Project(request):

    return render(request, "WebLucianoApp/project.html")