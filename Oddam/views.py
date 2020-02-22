from django.shortcuts import render

from django.db.models import Sum
from Oddam.models import Donation
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
        donations_number = Donation.objects.aggregate(Sum('quantity'))['quantity__sum']
        institutions_donated = Donation.objects.values('institution_id').distinct().count()

        return render(request, "Oddam/index.html", {'donations_number': donations_number,
                                                    'institutions_donated': institutions_donated})


class LoginView(View):
    def get(self, request):
        return render(request, "Oddam/login.html")


class RegisterView(View):
    def get(self, request):
        return render(request, "Oddam/register.html")
