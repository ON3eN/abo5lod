from django.db import models
from django.contrib.auth.models import User

ROLE_CHOICES = (
    ('youtuber', 'يوتيوبر'),
    ('editor', 'منتج'),
    ('designer', 'مصمم ثمنيل'),
    ('reviewer', 'مراجع'),
    ('uploader', 'مسؤول رفع'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="المستخدم")
    role = models.CharField("الدور", max_length=20, choices=ROLE_CHOICES)
    phone = models.CharField("رقم الجوال", max_length=20, blank=True)

    class Meta:
        verbose_name = "الملف الشخصي"
        verbose_name_plural = "الملفات الشخصية"

    def __str__(self):
        return f"{self.user.username} - {self.get_role_display()}"
