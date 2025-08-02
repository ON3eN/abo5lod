from django.contrib import admin
from .models import EditedVideo

@admin.register(EditedVideo)
class EditedVideoAdmin(admin.ModelAdmin):
    list_display = ('video', 'editor', 'uploaded_at')
