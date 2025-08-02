from django.db import models
from django.contrib.auth.models import User
from videos.models import Video

class EditedVideo(models.Model):
    video = models.OneToOneField(Video, on_delete=models.CASCADE, verbose_name="الفيديو الأصلي")
    editor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'profile__role': 'editor'}, verbose_name="المنتج")
    file = models.FileField("الفيديو بعد المونتاج", upload_to='edited_videos/')
    uploaded_at = models.DateTimeField("تاريخ الرفع", auto_now_add=True)
    notes_from_reviewer = models.TextField("ملاحظات المراجع", blank=True, null=True)

    class Meta:
        verbose_name = "فيديو منتج"
        verbose_name_plural = "الفيديوهات المنتجة"

    def __str__(self):
        return f"Edited: {self.video}"
