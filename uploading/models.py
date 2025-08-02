from django.db import models
from django.contrib.auth.models import User
from videos.models import Video

UPLOAD_STATUS_CHOICES = (
    ('not_started', 'لم يبدأ'),
    ('uploading', 'جاري الرفع'),
    ('uploaded', 'تم الرفع'),
)

class UploadStatus(models.Model):
    video = models.OneToOneField(Video, on_delete=models.CASCADE)
    uploader = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'profile__role': 'uploader'})
    status = models.CharField(max_length=20, choices=UPLOAD_STATUS_CHOICES, default='not_started')
    uploaded_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Upload status: {self.video} - {self.get_status_display()}"
