from django.contrib import admin
from .models import Video

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = (
        'uploader', 'upload_date', 'final_title', 'is_final_approved',
        'editor_status', 'thumbnail_status', 'review_status',
        'youtuber_status', 'uploading_status'
    )
    list_filter = ('is_final_approved', 'editor_status', 'thumbnail_status')
