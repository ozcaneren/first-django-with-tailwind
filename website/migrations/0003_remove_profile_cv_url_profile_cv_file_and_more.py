# Generated by Django 4.2.11 on 2025-07-17 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_sociallink_icon_type_alter_sociallink_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='cv_url',
        ),
        migrations.AddField(
            model_name='profile',
            name='cv_file',
            field=models.FileField(blank=True, help_text='PDF formatında CV dosyanızı yükleyin', null=True, upload_to='cv/', verbose_name='CV Dosyası (PDF)'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cv_image',
            field=models.ImageField(blank=True, help_text="CV'nin önizlemesi için resim (opsiyonel)", null=True, upload_to='profile/', verbose_name='CV Önizleme Resmi'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tech_stack',
            field=models.TextField(help_text='Her satırda bir teknoloji yazın. Örn:\nPython\nDjango\nJavaScript', verbose_name='Teknoloji Yığını (Her satırda bir teknoloji)'),
        ),
    ]
