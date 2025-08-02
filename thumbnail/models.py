from django.db import models
from django.contrib.auth.models import User
from videos.models import Video

class Thumbnail(models.Model):
    video = models.OneToOneField(Video, on_delete=models.CASCADE, verbose_name="الفيديو المرتبط")
    designer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'profile__role': 'designer'}, verbose_name="مصمم الثمنيل")
    image = models.ImageField("الصورة المصغرة", upload_to='thumbnails/')
    uploaded_at = models.DateTimeField("تاريخ الرفع", auto_now_add=True)
    notes_from_reviewer = models.TextField("ملاحظات المراجع", blank=True, null=True)

    class Meta:
        verbose_name = "ثمنيل"
        verbose_name_plural = "الثمنيلات"

    def __str__(self):
        return f"Thumbnail for {self.video}"
