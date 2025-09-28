from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
from .models import Users, Profile
from django.views import View



class HomeView(View):
    template_name = "app/index.html"

    def get(self, request: HttpRequest):
        appses = Profile.objects.all()
        userses = Users.objects.all()
        context = {
            "appses" : appses,
            "userses" : userses,
            "title" : "Barcha malumotlar"
        }
        return render(request, self.template_name, context)

