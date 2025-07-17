# Portfolio Website - Next.js to Django Migration

## Demo Link

https://web-production-c341.up.railway.app/

Bu proje, Next.js ile yazılmış bir portfolio websitesinin Django'ya çevrilmesi ve admin paneli ile güçlendirilmesi sürecini göstermektedir. Geliştirme sürecinde AI asistanından yardım alınmıştır.

## 🔄 Proje Geçişi

- **Önceki Durum**: Next.js + React + JavaScript
- **Şimdiki Durum**: Django + Python + Admin Panel

## 🛠 Kullanılan Teknolojiler

### Backend
- **Django** - Web framework
- **Python** - Programming language
- **SQLite** - Database
- **Pillow** - Image processing

### Frontend
- **Django Templates** - Template engine
- **Tailwind CSS** - CSS framework
- **Inter Font** - Typography
- **SVG Icons** - Vector graphics

## ✨ Özellikler

- **Dinamik İçerik**: Admin panelinden kolay yönetim
- **Profil Yönetimi**: Bio, tech stack, CV yükleme
- **Proje Showcase**: Hosting platform seçimi ile
- **Sosyal Medya**: SVG icon'lar ve özel logo desteği
- **Responsive Design**: Mobil uyumlu tasarım

## 🚀 Kurulum

```bash
# Repository'yi klonlayın
git clone [repository-url]

# Sanal ortam oluşturun
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Bağımlılıkları yükleyin
pip install django pillow

# Veritabanını oluşturun
python manage.py migrate

# Superuser oluşturun
python manage.py createsuperuser

# Server'ı başlatın
python manage.py runserver
```

## 📁 Proje Yapısı

```
├── mysite/                 # Django project settings
├── website/                # Main app
│   ├── models.py          # Profile, Project, SocialLink models
│   ├── views.py           # Home view
│   ├── admin.py           # Admin panel configuration
│   └── templates/         # HTML templates
├── media/                 # User uploaded files
└── static/               # Static files (CSS, images)
```

## 🎯 Ana Değişiklikler

1. **JSX → Django Templates**: React componentleri Django template'lere çevrildi
2. **Static → Dynamic**: Sabit kodlu içerik veritabanına taşındı
3. **Admin Panel**: İçerik yönetimi için Django admin eklendi
4. **File Upload**: CV ve resim yükleme sistemi
5. **SVG Icons**: Platform icon'ları SVG formatına çevrildi

## 🤖 AI Yardımı

Proje geliştirme sürecinde GitHub Copilot AI asistanından yardım alınmıştır:
- Next.js kodlarının Django'ya çevrilmesi
- Model tasarımı ve optimizasyonu
- Admin panel konfigürasyonu
- Template düzenlemeleri

---

This project demonstrates the migration of a Next.js portfolio website to Django with admin panel integration. AI assistance was utilized throughout the development process.

## 🔄 Migration Overview

- **Before**: Next.js + React + JavaScript
- **After**: Django + Python + Admin Panel

## 🛠 Tech Stack

**Backend**: Django, Python, SQLite, Pillow  
**Frontend**: Django Templates, Tailwind CSS, Inter Font, SVG Icons

## ✨ Features

- Dynamic content management via admin panel
- Profile management with bio, tech stack, CV upload
- Project showcase with hosting platform selection
- Social media links with SVG icons and custom logo support
- Responsive design

## 🤖 AI Assistance

GitHub Copilot AI assistant was used for:
- Converting Next.js code to Django
- Model design and optimization
- Admin panel configuration