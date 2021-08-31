from django.contrib import admin
from .models import Post
from .models import Contact, Category

# Register your models here.
admin.site.register((Contact, Category))

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyInject.js',)
