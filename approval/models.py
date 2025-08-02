from django.db import models
from django.contrib.auth.models import User
from videos.models import Video

class FinalApproval(models.Model):
    video = models.OneToOneField(Video, on_delete=models.CASCADE, verbose_name="الفيديو")
    youtuber = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'profile__role': 'youtuber'}, verbose_name="اليوتيوبر")
    approved = models.BooleanField("تمت الموافقة النهائية", default=False)
    notes = models.TextField("ملاحظات اليوتيوبر", blank=True)
    final_title = models.CharField("اسم الفيديو النهائي", max_length=255)
    approved_at = models.DateTimeField("تاريخ الموافقة", auto_now_add=True)

    class Meta:
        verbose_name = "موافقة نهائية"
        verbose_name_plural = "الموافقات النهائية"

    def __str__(self):
        return f"Final approval for {self.video}"
