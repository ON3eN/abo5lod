from django.db import models
from django.contrib.auth.models import User
from videos.models import Video

class Thumbnail(models.Model):
    video = models.OneToOneField(Video, on_delete=models.CASCADE)
    designer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'profile__role': 'designer'})
    image = models.ImageField(upload_to='thumbnails/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    notes_from_reviewer = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Thumbnail for {self.video}"
