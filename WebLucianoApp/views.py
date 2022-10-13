from django.shortcuts import render
from WebLucianoApp.models import ContactMe
from django.views.generic import CreateView
from WebLucianoApp.forms import FormContactMe



def Home(request):

    return render(request, "WebLucianoApp/home.html")


def About(request):

    return render(request, "WebLucianoApp/about-me.html")


def Project(request):

    return render(request, "WebLucianoApp/project.html")


class Page_create(CreateView):
    model = ContactMe
    #fields = '__all__'
    form_class = FormContactMe
    template = 'contactme_form.html'
    #context = {'mensaje':'creado'}
    