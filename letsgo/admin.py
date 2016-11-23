from django.contrib import admin
from letsgo.models import Places
from datetime import datetime, timedelta
# Register your models here.



@admin.register(Places)
class VenueAdmin(admin.ModelAdmin):
	list_display = ('time','place_id','formatted_time', 'name', 'checkins', 'herenow', 'category')
	list_filter = ('category','time',)




