from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.AccountView.as_view(),name='account-home'),

    path('register/',views.register,name='account-register'),
    path('login/',auth_views.LoginView.as_view(),name='account-login'),
    path('logout/',auth_views.LogoutView.as_view(),name='account-logout'),
    path('update-account/',views.AccountUpdateView.as_view(),name='account-update'),

    path('builds/',views.AccountView.as_view(), name='account-builds'),
]