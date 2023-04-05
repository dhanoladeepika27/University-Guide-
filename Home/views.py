from django.shortcuts import render
from Home.models import PagePosts


# Create your views here.


def homewpinfo(request):
    homegetwpinfo = PagePosts.objects.filter(url='home')
    return render(request, "index.html", {'homeposts': homegetwpinfo})


def librarywpinfo(request):
    librarygetwpinfo = PagePosts.objects.filter(url='library')
    return render(request, "library.html", {'libraryposts': librarygetwpinfo})


def itserviceswpinfo(request):
    itservicesgetwpinfo = PagePosts.objects.filter(url='it_services')
    return render(request, "it_services.html", {'itservicesposts': itservicesgetwpinfo})


def office365wpinfo(request):
    office365getwpinfo = PagePosts.objects.filter(url='office_365')
    return render(request, "office_365.html", {'office365posts': office365getwpinfo})


def microsoftteamswpinfo(request):
    microsoftteamsgetwpinfo = PagePosts.objects.filter(url='microsoft_teams')
    return render(request, "microsoft_teams.html", {'microsoftteamsposts': microsoftteamsgetwpinfo})


def universityemailwpinfo(request):
    universityemailgetwpinfo = PagePosts.objects.filter(url='university_email')
    return render(request, "university_email.html", {'universityemailposts': universityemailgetwpinfo})
