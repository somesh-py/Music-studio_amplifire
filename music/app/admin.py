from django.contrib import admin
from .models import MusicReg
# Register your models here.


@admin.register((MusicReg))
class MusicRegModelAdmin(admin.ModelAdmin):
    list_display=['id','name','artist','release_date','genre','audio','image','duration']