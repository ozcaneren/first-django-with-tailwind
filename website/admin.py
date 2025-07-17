from django.contrib import admin
from .models import Project, SocialLink, Profile

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'hosting_platform', 'is_active', 'created_at']
    list_filter = ['hosting_platform', 'is_active', 'created_at']
    list_editable = ['is_active']
    search_fields = ['title', 'description']
    
    fieldsets = (
        ('Proje Bilgileri', {
            'fields': ('title', 'description', 'url', 'image', 'is_active')
        }),
        ('Hosting & Görünüm', {
            'fields': ('hosting_platform', 'custom_logo', 'background_color')
        }),
    )
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['background_color'].help_text = "Örnek: bg-blue-100, bg-green-50, bg-purple-100"
        return form

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'username', 'icon_type', 'url', 'is_active', 'order']
    list_filter = ['is_active', 'name', 'icon_type']
    list_editable = ['is_active', 'order']
    ordering = ['order']
    
    fieldsets = (
        ('Temel Bilgiler', {
            'fields': ('name', 'username', 'url', 'is_active', 'order')
        }),
        ('Icon Ayarları', {
            'fields': ('icon_type', 'icon'),
            'description': 'SVG icon kullanmak için icon türünü seçin, özel icon için resim yükleyin.'
        }),
        ('Görünüm', {
            'fields': ('background_color', 'button_color'),
            'description': 'Tailwind CSS class\'ları kullanın (ör: bg-blue-100, bg-red-500)'
        }),
    )

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title']
    
    fieldsets = (
        ('Temel Bilgiler', {
            'fields': ('name', 'title', 'bio')
        }),
        ('Teknoloji Yığını', {
            'fields': ('tech_stack',),
            'description': 'Her satırda bir teknoloji yazın. Örnek:\nPython\nDjango\nJavaScript'
        }),
        ('Dosyalar', {
            'fields': ('profile_image', 'cv_file', 'cv_image'),
            'description': 'Profil resmi zorunlu. CV dosyası PDF olmalı. CV resmi opsiyonel.'
        }),
    )
    
    def has_add_permission(self, request):
        # Sadece bir profil olmasını sağla
        return not Profile.objects.exists()
    
    def has_delete_permission(self, request, obj=None):
        # Profil silinmesin
        return False
