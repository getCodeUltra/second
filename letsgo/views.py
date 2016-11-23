# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.conf import settings
from letsgo.models import Places
import foursquare
import logging
from datetime import datetime, timedelta

# Get an instance of a logger
logger = logging.getLogger(__name__)
#coding=utf-8
# Create your views here.

client = foursquare.Foursquare(
	client_id='VT0RZ3JARS00WR4BXCY44GJPRC4VO3FXPTJX2FMMX14MMYDE', 
	client_secret='GSLTNFEZP4BUWAZNBHHUJVG2TADP25QTQWDAZQTTMBFJHXIN'
	)


def home(request, lang=None):
	return render_to_response(
		'home.html',)

def index(request):
	
	response = client.venues.search(
		params={'ll': '39.9232611,32.859479',
		 'ne': '39.9283391,32.861201',
		 'sw': '39.9188267,32.8588045',
		 'limit': 50}
	)

	for i in range(0,len(response.get('venues'))):
		Places.objects.create(
			name=response.get('venues')[i].get('name'),
			formatted_time=datetime.now().strftime('%y%m%d'),
			place_id=response.get('venues')[i].get('id'),
			checkins=response.get('venues')[i].get('stats').get('checkinsCount'),
			herenow=response.get('venues')[i].get('hereNow').get('count'),
			category=response.get('venues')[i].get('categories')[0].get('name'),
			)
	return HttpResponseRedirect('/admin/letsgo/places')


			


	
	
