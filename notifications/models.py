from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications', verbose_name="المستخدم")
    message = models.CharField("نص الإشعار", max_length=255)
    link = models.URLField("رابط", blank=True, null=True)
    created_at = models.DateTimeField("تاريخ الإشعار", auto_now_add=True)
    read = models.BooleanField("تمت قراءته؟", default=False)

    class Meta:
        verbose_name = "إشعار"
        verbose_name_plural = "الإشعارات"

    def __str__(self):
        return f"Notification for {self.user.username}"
