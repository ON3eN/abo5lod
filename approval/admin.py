from django.contrib import admin
from .models import FinalApproval

@admin.register(FinalApproval)
class FinalApprovalAdmin(admin.ModelAdmin):
    list_display = ('video', 'youtuber', 'final_title', 'approved', 'approved_at')
