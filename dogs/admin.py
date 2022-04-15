from django.contrib import admin
from .models import Dog
from django.utils.html import format_html

# Register your models here.

class DogAdmin(admin.ModelAdmin):
    #show image thumbnail in admin
    def thumbnail(self, object):
        return format_html('<img src="{}" width = "40px" />'.format(object.dog_photo.url))
    thumbnail.short_description = 'Dog image'
   
    #display list in admin
    list_display = ('id', 'thumbnail', 'gender', 'state','bread_name','is_featured')
    list_display_links = ('id','bread_name',)
    list_editable = ('is_featured',)
    search_fields = ('bread_name','location')
    list_filter = ('gender','city','bread_name')


admin.site.register(Dog, DogAdmin)
