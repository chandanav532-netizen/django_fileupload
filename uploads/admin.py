from django.contrib import admin
from .models import document
@admin.register(document) 
class DocumentAdmin(admin.ModelAdmin):    
    list_display = ('title', 'file', 'uploaded_at')