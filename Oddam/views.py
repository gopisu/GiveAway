from django.shortcuts import render

from django.db.models import Sum
from Oddam.models import Donation, Institution
from django.views import View
import random

class AddDonationView(View):
    def get(self, request):
        return render(request, "Oddam/form.html")


class ConfirmationView(View):
    def get(self, request):
        return render(request, "Oddam/form-confirmation.html")


class LandingPageView(View):
    def get(self, request):
        donations_number = Donation.objects.aggregate(Sum('quantity'))['quantity__sum']
        institutions_donated = Donation.objects.values('institution_id').distinct().count()
        random_fund = Institution.objects.all().filter(type='FUND').order_by("?")[:3]
        random_org = Institution.objects.all().filter(type='ORG').order_by("?")[:4]
        random_gat = Institution.objects.all().filter(type='GAT').order_by("?")[:3]
        return render(request, "Oddam/index.html", {'donations_number': donations_number,
                                                    'institutions_donated': institutions_donated,
                                                    'random_fund': random_fund,
                                                    'random_gat': random_gat,
                                                    'random_org': random_org})


class LoginView(View):
    def get(self, request):
        return render(request, "Oddam/login.html")


class RegisterView(View):
    def get(self, request):
        return render(request, "Oddam/register.html")
