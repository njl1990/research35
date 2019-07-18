from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='Index'),
	path('hstr', views.Hstr, name='Hstr'),
	path('index.html', views.Index, name='Index'),

# API
	#Load 
	path('LoadPreData', views.LoadPreData, name='LoadPreData'),
	path('LoadReply', views.LoadReply, name='LoadReply'),
	path('Reply', views.Reply, name='Reply'),
	#path('HeartBeat', views.HeartBeat, name='HeartBeat'),
]