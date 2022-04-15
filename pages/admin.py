from django.contrib import admin

#from pages.models import Teams
from django.contrib import admin
from .models import Farm_bread, dog_slider
from django.utils.html import format_html

# Register your models here.

class Farm_breadAdmin(admin.ModelAdmin):
    #show image thumbnail in admin
    def thumbnail(self, object):
        return format_html('<img src="{}" width = "40px" />'.format(object.photo.url))
    thumbnail.short_description = 'Photo'
   
    #display list in admin
    list_display = ('id', 'thumbnail', 'age', 'location','bread_name')
    list_display_links = ('id','bread_name',)
    search_fields = ('bread_name','location')

admin.site.register(Farm_bread, Farm_breadAdmin )

class dog_sliderAdmin(admin.ModelAdmin):
    #show image of slider in admin
    def thumbnail(self, object):
        return format_html('<img src="{}" width = "40px" />'.format(object.slider.url))
    thumbnail.short_description ='slider'

    #display list of slider in admin
    list_display =('id','thumbnail','slider_name')
    list_display_links = ('id','thumbnail','slider_name',)

admin.site.register(dog_slider, dog_sliderAdmin)
