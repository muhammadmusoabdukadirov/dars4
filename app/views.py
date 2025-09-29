from django.shortcuts import render, get_list_or_404, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
# Create your views here.
from django.views.generic import ListView, DetailView, View, CreateView, UpdateView, DeleteView
from .models import Users, Profile, Resume
from django.views import View
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from .forms import ResumeForm


# bu klas hamma modeldagi malumotni chiqarish uchun
class HomeView(View):
    template_name = "app/index.html"

    def get(self, request):
        appses = Profile.objects.all()
        userses = Users.objects.all()
        resumes = Resume.objects.all().order_by('-created_at') 

        context = {
            "appses": appses,
            "userses": userses,
            "resumes": resumes, 
        }
        return render(request, self.template_name, context)
    

# Resume List
class ResumeListView(ListView):
    model = Resume
    template_name = "resume_list.html"
    context_object_name = "resumes"
    ordering = ["-created_at"]


# Resume Detail
class ResumeDetailView(DetailView):
    model = Resume
    template_name = "app/resume_detail.html"
    context_object_name = "resume"


# habar yuborish
class ContactResumeView(View):
    template_name = "app/contact_resume.html"  # app papkasini qo‘shishni unutmang

    def get(self, request, pk):
        resume = get_object_or_404(Resume, pk=pk)
        return render(request, self.template_name, {"resume": resume})

    def post(self, request, pk):
        resume = get_object_or_404(Resume, pk=pk)
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        sender_email = request.POST.get("email")

        full_message = f"From: {sender_email}\n\n{message}"

        send_mail(
            subject,
            full_message,
            settings.DEFAULT_FROM_EMAIL,
            [resume.email],
            fail_silently=False,
        )

        return redirect("resume_detail", pk=resume.pk)
    
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Resume

class ResumeListView(ListView):
    model = Resume
    template_name = 'app/resume_list.html'
    context_object_name = 'resumes'

class ResumeDetailView(DetailView):
    model = Resume
    template_name = 'app/resume_detail.html'
    context_object_name = 'resume'

class ResumeCreateView(CreateView):
    model = Resume
    fields = '__all__'
    template_name = 'app/resume_form.html'
    success_url = reverse_lazy('index')  

class ResumeUpdateView(UpdateView):
    model = Resume
    form_class = ResumeForm
    template_name = 'app/resume_form.html'
    success_url = reverse_lazy('resume_list')

class ResumeDeleteView(DeleteView):
    model = Resume
    template_name = 'app/resume_confirm_delete.html'
    success_url = reverse_lazy('resume_list')