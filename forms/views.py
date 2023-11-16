from django.shortcuts import render, redirect
from django.views import generic


from .models import Form
from .forms import MyForm
from django.urls import reverse_lazy


class FormCreateView(generic.CreateView):
    
    form_class = MyForm
    template_name = 'form.html'
    success_url = "/admin/"