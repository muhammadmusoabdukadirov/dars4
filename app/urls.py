from django.urls import path
from .views import (
    HomeView,
    ResumeListView,
    ResumeDetailView,
    ContactResumeView,
    ResumeCreateView,
    ResumeUpdateView,
    ResumeDeleteView,
)

urlpatterns = [
    # Bosh sahifa
    path('', HomeView.as_view(), name='index'),

    # Resume ro'yxati
    path('resumes/', ResumeListView.as_view(), name='resume_list'),

    # Resume qo'shish
    path('resumes/add/', ResumeCreateView.as_view(), name='resume_add'),

    # Resume detallari
    path('resumes/<int:pk>/', ResumeDetailView.as_view(), name='resume_detail'),

    # Resume taxrirlash
    path('resumes/<int:pk>/edit/', ResumeUpdateView.as_view(), name='resume_edit'),

    # Resume o'chirish
    path('resumes/<int:pk>/delete/', ResumeDeleteView.as_view(), name='resume_delete'),

    # Resume egasiga xabar yuborish
    path('resumes/<int:pk>/contact/', ContactResumeView.as_view(), name='contact_resume'),
]
