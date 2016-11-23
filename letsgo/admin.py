from django.contrib import admin
from letsgo.models import Places, Cafe
from datetime import datetime, timedelta
# Register your models here.



@admin.register(Places)
class VenueAdmin(admin.ModelAdmin):
	list_display = ('time','place_id','formatted_time', 'name', 'checkins', 'herenow', 'category')
	#ordering = ['category']
	actions = [show_last_day,show_last_week]
	list_filter = ('category','time',)




