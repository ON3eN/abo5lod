"""
URL configuration for abo_5lod project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('abo5lod3en38/', admin.site.urls),

    # تطبيقات المشروع الخاصة
    path('', include('core.urls')),               # الصفحة الرئيسية ولوحة التحكم
    path('account/', include('account.urls')),    # تسجيل الدخول، الصلاحيات، الحسابات
    path('videos/', include('videos.urls')),      # رفع الفيديوهات وتتبعها
    path('editor/', include('editor.urls')),      # مهام المنتج (المونتاج)
    path('thumbnail/', include('thumbnail.urls')),# مهام مصمم الثمنيل
    path('review/', include('review.urls')),      # مراجعة الفيديو والصورة
    path('approval/', include('approval.urls')),  # رأي اليوتيوبر النهائي
    path('uploading/', include('uploading.urls')),# رفع الملفات لليوتيوب
    path('chat/', include('chat.urls')),          # المحادثات الجماعية
    path('notifications/', include('notifications.urls')), # الإشعارات
]
