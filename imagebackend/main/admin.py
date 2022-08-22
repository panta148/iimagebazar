from django.contrib import admin

from .models import Catrgory, Images


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'time']


admin.site.register(Catrgory, CategoryAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ['category', 'image_tag', 'time']


admin.site.register(Images, ImageAdmin)
