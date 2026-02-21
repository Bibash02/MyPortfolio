from django.contrib import admin
from .models import ContactMessage

# Register your models here.
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'subject', 'budget', 'message', 'created_at', 'is_read')
    list_filter = ('subject', 'budget', 'created_at', 'is_read')
    search_fields = ('first_name', 'last_name', 'email', 'message')