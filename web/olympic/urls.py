from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='Index'),
	path('hstr-yy1', views.HsytYY1, name='HsytYY1'),
	path('hstr-nongyao1', views.HsytNY1, name='nongyao1'),
	path('index.html', views.Index, name='Index'),
# API
	#Load 
	path('LoadReply', views.LoadReply, name='LoadReply'),
	path('Reply', views.Reply, name='Reply'),
	#path('HeartBeat', views.HeartBeat, name='HeartBeat'),
]