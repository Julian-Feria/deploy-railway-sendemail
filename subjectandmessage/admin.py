from django.contrib import admin
from .models import SubjectAndMessage

@admin.register(SubjectAndMessage)
class SubjectAndMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'message')