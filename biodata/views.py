from django.views.generic import ListView
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm
from .models import Bio, Education, Work, Project

# Create your views here.


class IndexView(ListView):
    context_object_name = 'biodata'
    template_name = 'index.html'
    queryset = Bio.objects.all()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['education'] = Education.objects.all()
        context['work'] = Work.objects.all()
        context['project'] = Project.objects.all()
        return context
