from django.contrib import admin
from .models import News_post

class NewsPostAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change:  # Если создается новая запись
            obj.username = request.user
        obj.save()

admin.site.register(News_post, NewsPostAdmin)


