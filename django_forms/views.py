from django.shortcuts import render
from . import forms


def index(request):
    form = forms.ContactForm()

    context = {
        'form': form
    }
    return render(request, 'django_forms/index.html', context)
