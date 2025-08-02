from django.db import models
from django.contrib.auth.models import User
from videos.models import Video

class Review(models.Model):
    video = models.OneToOneField(Video, on_delete=models.CASCADE, verbose_name="الفيديو")
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'profile__role': 'reviewer'}, verbose_name="المراجع")
    reviewed_at = models.DateTimeField("تاريخ المراجعة", auto_now_add=True)

    editor_approved = models.BooleanField("تمت الموافقة على الفيديو", default=False)
    editor_notes = models.TextField("ملاحظات على الفيديو", blank=True)

    thumbnail_approved = models.BooleanField("تمت الموافقة على الثمنيل", default=False)
    thumbnail_notes = models.TextField("ملاحظات على الثمنيل", blank=True)

    class Meta:
        verbose_name = "مراجعة"
        verbose_name_plural = "المراجعات"

    def __str__(self):
        return f"Review for {self.video}"
