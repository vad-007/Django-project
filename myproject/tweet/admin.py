from django.contrib import admin
from .models import Tweet
# Register your models here.

from django.utils.html import format_html

class TweetAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'photo_thumbnail', 'created_at')

    def photo_thumbnail(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.photo.url)
        return "No Image"
    photo_thumbnail.short_description = 'Photo Preview'

admin.site.register(Tweet, TweetAdmin)
