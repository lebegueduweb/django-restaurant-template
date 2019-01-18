from django.contrib import admin

from .models import Post, Carousel, Service, MotGerante

admin.site.register(Post)
admin.site.register(Carousel)
admin.site.register(Service)
admin.site.register(MotGerante)

class CarouselAdmin(admin.ModelAdmin):
    list_display = "__all__"


    fieldsets = (
        (None, {
            'fields': ('diaporama_image', 'diaporama_description')
        }),
    )