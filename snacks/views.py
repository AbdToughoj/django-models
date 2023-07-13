from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Snack_List_View(TemplateView):
    template_name = 'snack_list.html'