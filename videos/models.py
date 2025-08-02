from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ('pending', 'بانتظار البدء'),
    ('in_progress', 'قيد التنفيذ'),
    ('completed', 'تم الانتهاء'),
)

class Video(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_videos', verbose_name="اليوتيوبر")
    file = models.FileField("ملف الفيديو", upload_to='videos/')
    upload_date = models.DateTimeField("تاريخ الرفع", auto_now_add=True)
    final_title = models.CharField("العنوان النهائي", max_length=255, blank=True)
    is_final_approved = models.BooleanField("تمت الموافقة النهائية", default=False)

    editor_status = models.CharField("حالة المنتج", max_length=20, choices=STATUS_CHOICES, default='pending')
    thumbnail_status = models.CharField("حالة المصمم", max_length=20, choices=STATUS_CHOICES, default='pending')
    review_status = models.CharField("حالة المراجع", max_length=20, choices=STATUS_CHOICES, default='pending')
    youtuber_status = models.CharField("حالة اليوتيوبر", max_length=20, choices=STATUS_CHOICES, default='pending')
    uploading_status = models.CharField("حالة الرفع", max_length=20, choices=STATUS_CHOICES, default='pending')

    class Meta:
        verbose_name = "فيديو"
        verbose_name_plural = "الفيديوهات"

    def __str__(self):
        return f"Video by {self.uploader.username} at {self.upload_date.strftime('%Y-%m-%d')}"
