from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='django-forms-index'),
]
