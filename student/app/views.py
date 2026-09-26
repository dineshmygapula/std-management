from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from app.models import Company
from app.forms import CompanyForm, RegistrationForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required


# Create your views here.
class CompanyView(LoginRequiredMixin, TemplateView):
    template_name = "employees_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "company profile"
        company_deltails = Company.objects.all()
        context["company_details"] = company_deltails
        return context


@login_required
def create_company(request):
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("company_list")
    else:
        form = CompanyForm()
    return render(request, "create.html", context={"form": form})


@login_required
def company_list(request):
    companies = Company.objects.all()
    return render(request, "company_list.html", context={"companies": companies})


@login_required
def update_company(request, id):
    company = Company.objects.get(id=id)
    if request.method == "POST":
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            form.save()
            return redirect("company_list")
    else:
        form = CompanyForm(instance=company)
    return render(request, "update.html", context={"form": form, "company": company})


@login_required
def delete_company(request, id):
    company = Company.objects.get(id=id)
    if request.method == "POST":
        if company.logo:
            company.logo.delete(save=False)
        company.delete()
        return redirect("company_list")
    return render(request, "delete_company.html", context={"company": company})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "register.html", context={"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("company_list")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", context={"form": form})


def user_logout(request):
    logout(request)
    return redirect("login")


def session_demo(request):
    request.session["name"] = "Dinesh"
    return HttpResponse("Session created")


def show_session(request):
    name = request.session.get("name")
    return HttpResponse(f"Hello {name}")


@permission_required("app.can_approve_company")
def approve_company(request, id):
    company = Company.objects.get(id=id)
    company.approved = True
    company.save()
    return redirect("company_list")


@permission_required("app.can_delete_company")
def delete_company(request, id):
    company = Company.objects.get(id=id)
    company.delete()
    return redirect("company_list")
