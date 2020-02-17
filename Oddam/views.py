from django.shortcuts import render

# Create your views here.
from django.views import View


class TestView(View):
    def get(self, request):
        return render(request, "Oddam/__base__.html")


class LandingPageView(View):
    def get(self, request):
        return render(request, "Oddam/form.html")


class ConfirmationView(View):
    def get(self, request):
        return render(request, "Oddam/form-confirmation.html")


class AddDonationView(View):
    def get(self, request):
        return render(request, "Oddam/index.html")


class LoginView(View):
    def get(self, request):
        return render(request, "Oddam/login.html")


class RegisterView(View):
    def get(self, request):
        return render(request, "Oddam/register.html")
