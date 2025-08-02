from django.contrib import admin
from .models import UploadStatus

@admin.register(UploadStatus)
class UploadStatusAdmin(admin.ModelAdmin):
    list_display = ('video', 'uploader', 'status', 'uploaded_at')
    list_filter = ('status',)
