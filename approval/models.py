from django.db import models
from django.contrib.auth.models import User
from videos.models import Video

class FinalApproval(models.Model):
    video = models.OneToOneField(Video, on_delete=models.CASCADE)
    youtuber = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'profile__role': 'youtuber'})
    approved = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    final_title = models.CharField(max_length=255)
    approved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Final approval for {self.video}"
