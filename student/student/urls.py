"""
URL configuration for student project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from app.views import (
    CompanyView,
    create_company,
    company_list,
    update_company,
    delete_company,
    register,
    user_login,
    user_logout,
    session_demo,
    show_session,
)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from app.asy import async_home, async_company, company1, github_user

urlpatterns = [
    path("admin/", admin.site.urls),
    path("company/", CompanyView.as_view(), name="company"),
    path("create_company/", create_company, name="create_company"),
    path("companies/", company_list, name="company_list"),
    path("update/<int:id>/", update_company, name="update_company"),
    path("delete/<int:id>/", delete_company, name="delete_company"),
    path("login/", user_login, name="login"),
    path("register/", register, name="register"),
    path("logout/", user_logout, name="logout"),
    path("session_demo/", session_demo, name="session_demo"),
    path("show_session/", show_session, name="show_session"),
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
        name="password_reset",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path("async/", async_home, name="async_home"),
    path("asynccompany/", async_company, name="asynccompany"),
    path("comp/", company1, name="comp"),
    path("githubuser/", github_user),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
