from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView, FormView
from django.urls import reverse_lazy
from .forms import RegistrationForm


def index(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


def registration(request):
    return render(request, 'registration.html')


def AboutAsView(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = RegistrationForm()
    return render(request, 'about_as.html', {'form': form})

# class AboutAsView(FormView):
# form_class = RegistrationForm
# success_url = reverse_lazy('success')
#  template_name = 'about_as.html'
