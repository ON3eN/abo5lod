from django.db import models
from django.contrib.auth.models import User
from videos.models import Video

UPLOAD_STATUS_CHOICES = (
    ('not_started', 'لم يبدأ'),
    ('uploading', 'جاري الرفع'),
    ('uploaded', 'تم الرفع'),
)

class UploadStatus(models.Model):
    video = models.OneToOneField(Video, on_delete=models.CASCADE, verbose_name="الفيديو")
    uploader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'profile__role': 'uploader'}, verbose_name="مسؤول الرفع")
    status = models.CharField("الحالة", max_length=20, choices=UPLOAD_STATUS_CHOICES, default='not_started')
    uploaded_at = models.DateTimeField("تاريخ الرفع", blank=True, null=True)

    class Meta:
        verbose_name = "حالة الرفع"
        verbose_name_plural = "حالات الرفع"

    def __str__(self):
        return f"Upload status: {self.video} - {self.get_status_display()}"
