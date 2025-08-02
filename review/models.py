from django.db import models
from django.contrib.auth.models import User
from videos.models import Video

class Review(models.Model):
    video = models.OneToOneField(Video, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'profile__role': 'reviewer'})
    reviewed_at = models.DateTimeField(auto_now_add=True)

    # مراجعة لكل جزء
    editor_approved = models.BooleanField(default=False)
    editor_notes = models.TextField(blank=True)

    thumbnail_approved = models.BooleanField(default=False)
    thumbnail_notes = models.TextField(blank=True)

    def __str__(self):
        return f"Review for {self.video}"
