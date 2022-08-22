from django.db import models
from django.utils.safestring import mark_safe


class Catrgory(models.Model):
    title = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.title


class Images(models.Model):
    category = models.ForeignKey(Catrgory, on_delete=models.CASCADE)
    image = models.ImageField(
        blank=True, default='no inage', upload_to='pictures/')
    time = models.DateTimeField(auto_now_add=True)

    def image_tag(self):
        msg = '<img src="{}" style="{}" height="20" width="20"/>'.format(
            self.image.url, "object-fit: contain;")
        return mark_safe(msg)
    image_tag.short_description = 'Image'

    class Meta:
        verbose_name_plural = 'Image'

    def __str__(self):
        return f'[{self.category.title}]  images'
