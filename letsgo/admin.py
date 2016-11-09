from django.contrib import admin
from letsgo.models import Places, Cafe
from datetime import datetime, timedelta
# Register your models here.



def show_last_day(modelAdmin, request, queryset):
	
	Places.objects.filter(time=datetime.today())

show_last_day.short_description="Show checkins from last day"

def show_last_week(modelAdmin, request, queryset):

	last_week=(datetime.today() - timedelta(days=7))
	Places.objects.filter(time__lt=last_week)

show_last_week.short_description="Show checkins form last week"
#def show_last_month(modelAdmin, request, queryset):

@admin.register(Places)
class VenueAdmin(admin.ModelAdmin):
	list_display = ('time','place_id','formatted_time', 'name', 'checkins', 'herenow', 'category')
	#ordering = ['category']
	actions = [show_last_day,show_last_week]

@admin.register(Cafe)
class CafeAdmin(admin.ModelAdmin):
	list_display = ('time','place_id', 'name', 'herenow', 'checkins')


