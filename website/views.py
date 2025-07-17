from django.shortcuts import render

def home(request):
    """Ana sayfa görünümü"""
    return render(request, 'website/home.html')

def about(request):
    """Hakkımızda sayfası görünümü"""
    return render(request, 'website/about.html')

def contact(request):
    """İletişim sayfası görünümü"""
    return render(request, 'website/contact.html')
