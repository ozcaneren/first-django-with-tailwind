from django.shortcuts import render
from .models import Project, SocialLink, Profile

def home(request):
    """Ana sayfa görünümü"""
    profile = Profile.objects.first()
    projects = Project.objects.all()  # is_active kaldırdık
    social_links = SocialLink.objects.filter(is_active=True).order_by('order')
    
    context = {
        'profile': profile,
        'projects': projects,
        'social_links': social_links,
    }
    return render(request, 'website/home.html', context)
