from django.contrib import admin
from .models import Locations,Girls
@admin.register(Locations)
class LocationsControl(admin.ModelAdmin):
    fields=['name','slug']
    list_display=['name','slug','id']
@admin.register(Girls)
class GirlsControl(admin.ModelAdmin):
    search_fields = ['name']
    fields=['name','loc','img','img2','img3','img4','img5','img6','img7','img8','img9','img10','num','numlink','desc','date','slug']
    list_filter=['date','loc']
    list_display=['name','loc','slug']