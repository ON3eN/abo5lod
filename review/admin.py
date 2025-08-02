from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'video', 'reviewer', 'reviewed_at',
        'editor_approved', 'thumbnail_approved'
    )
