from django.db import models
from django.contrib.auth.models import User
from videos.models import Video

class ChatMessage(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField(upload_to='chat_attachments/', blank=True, null=True)

    def __str__(self):
        return f"{self.sender} - {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
