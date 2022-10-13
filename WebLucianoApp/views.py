from django.shortcuts import render
from WebLucianoApp.models import ContactMe
from django.views.generic import CreateView



def Home(request):

    return render(request, "WebLucianoApp/home.html")


def About(request):

    return render(request, "WebLucianoApp/about-me.html")


def Project(request):

    return render(request, "WebLucianoApp/project.html")


class Page_create(CreateView):
    model = ContactMe
    fields = '__all__'
    #form_class = PostForm
    template = 'post_form.html'
    #context = {'mensaje':'creado'}
    