from django.contrib import admin
from .models import Thumbnail

@admin.register(Thumbnail)
class ThumbnailAdmin(admin.ModelAdmin):
    list_display = ('video', 'designer', 'uploaded_at')
