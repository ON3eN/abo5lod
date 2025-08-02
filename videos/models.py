from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ('pending', 'بإنتظار البدء'),
    ('in_progress', 'قيد التنفيذ'),
    ('completed', 'تم الانتهاء'),
)

class Video(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_videos')
    file = models.FileField(upload_to='videos/')
    upload_date = models.DateTimeField(auto_now_add=True)
    final_title = models.CharField(max_length=255, blank=True)
    is_final_approved = models.BooleanField(default=False)

    # مؤشرات الحالة
    editor_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    thumbnail_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    review_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    youtuber_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    uploading_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Video by {self.uploader.username} at {self.upload_date.strftime('%Y-%m-%d')}"
