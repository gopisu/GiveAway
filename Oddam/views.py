from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views import View

from Oddam.models import Donation, Institution, Category
from Oddam.utils import (
    check_passwords_match,
    NotMatchingPasswordsError,
    ERROR_MESSAGE,
)


class AddDonationView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request):
        categories = Category.objects.all()
        institutions = Institution.objects.all()
        return render(
            request,
            "Oddam/form.html",
            context={"categories": categories, "institutions": institutions},
        )
    def post(self, request):
        categories = request.POST.get("category")
        bags = request.POST.get("bags")
        organization = request.POST.get("organization")
        address = request.POST.get("address")
        city = request.POST.get("city")
        postcode = request.get("postcode")
        phone = request.get("phone")
        data = request.get("data")
        time = request.get("time")
        more_info = request.more_info("more_info")
        new_donation = Donation.objects.create(
            quantity=bags,
            institution=organization,
            address=address,
            city=city,
            postcode=postcode,
            phone_number=phone,
            pick_up_comment=more_info,
            pick_up_date=data,
            pick_up_time=time,
        )
        return render(
            request,
            "Oddam/form-confirmation.html"
        )

class ConfirmationView(View):
    def get(self, request):
        return render(request, "Oddam/form-confirmation.html")




class LandingPageView(View):
    def get(self, request):
        donations_number = Donation.objects.aggregate(Sum("quantity"))["quantity__sum"]
        institutions_donated = (
            Donation.objects.values("institution_id").distinct().count()
        )
        random_fund = Institution.objects.all().filter(type="FUND").order_by("?")[:3]
        random_org = Institution.objects.all().filter(type="ORG").order_by("?")[:4]
        random_gat = Institution.objects.all().filter(type="GAT").order_by("?")[:3]
        return render(
            request,
            "Oddam/index.html",
            {
                "donations_number": donations_number,
                "institutions_donated": institutions_donated,
                "random_fund": random_fund,
                "random_gat": random_gat,
                "random_org": random_org,
            },
        )


class LoginView(View):
    def get(self, request):
        return render(request, "Oddam/login.html")

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(username=email, password=password)
        if User.objects.filter(email=email).count() < 1:
            return redirect("register")
        elif user is not None:
            login(request, user)
            return redirect("landing-page")
        else:
            message = ERROR_MESSAGE["not_authenticted"]
            return render(request, "Oddam/login.html", context={"message": message})


class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        return redirect("landing-page")


class UserView(View):
    def get(self, request):
        user = User.objects.get(username=request.user.username)
        donations = Donation.objects.filter(user=user)
        return render(request, "Oddam/user.html", context={"donations": donations})


class RegisterView(View):
    def get(self, request):
        return render(request, "Oddam/register.html")

    def post(self, request):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        try:
            check_passwords_match(password, password2)
            User.objects.create_user(
                email=email,
                username=email,
                first_name=first_name,
                last_name=last_name,
                password=password,
            )
            return redirect("login")
        except IntegrityError:
            message = ERROR_MESSAGE["user_exists"]
        except NotMatchingPasswordsError:
            message = ERROR_MESSAGE["passwords_not_matching"]
        except ValueError:
            message = ERROR_MESSAGE["empty_email"]
        return render(request, "registration", context={"message": message})
