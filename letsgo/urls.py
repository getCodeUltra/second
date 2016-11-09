from django.conf.urls import url
from . import views




urlpatterns=[
	url(r'^$', 'letsgo.views.index'),
	url(r'^$', 'letsgo.views.cafe'),
	#url(r'^feature/$', 'letsgo.views.make_featured', name='feature'),
	#url(r'^count_likes/$', 'letsgo.views.count_like', name='count_likes'),
]
