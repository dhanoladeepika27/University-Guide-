"""Hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from Home import views

urlpatterns = [
    # path('', views.index, name='home'),
    # path('home', views.index, name='home'),
    # path('library', views.library, name='library'),
    # path('it_services', views.it_services, name='it_services'),
    # path('office_365', views.office_365, name='office_365'),
    # path('microsoft_teams', views.microsoft_teams, name='microsoft_teams'),
    # path('university_email', views.university_email, name='university_email'),

    path('', views.homewpinfo),
    path('home', views.homewpinfo),
    path('library', views.librarywpinfo),
    path('it_services', views.itserviceswpinfo),
    path('office_365', views.office365wpinfo),
    path('microsoft_teams', views.microsoftteamswpinfo),
    path('university_email', views.universityemailwpinfo),
]
