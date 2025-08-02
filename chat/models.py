from django.db import models
from django.contrib.auth.models import User
from videos.models import Video

class ChatMessage(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, verbose_name="الفيديو")
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="المرسل")
    message = models.TextField("الرسالة")
    timestamp = models.DateTimeField("الوقت", auto_now_add=True)
    attachment = models.FileField("مرفق", upload_to='chat_attachments/', blank=True, null=True)

    class Meta:
        verbose_name = "رسالة محادثة"
        verbose_name_plural = "رسائل المحادثة"

    def __str__(self):
        return f"{self.sender} - {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
