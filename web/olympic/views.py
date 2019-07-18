from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.template import loader
from bson.objectid import ObjectId
from bson import json_util
from pymongo import MongoClient
import time

def Index(request):
	mongoClient = MongoClient('research35.db',27017)
	#mongoClient = MongoClient('192.168.0.153',27017)
	DBClient = mongoClient['olympicdb']
	collection = DBClient['activitydata']
	ActivityData=collection.find({})
	ActivityList=[]
	for item in ActivityData:
		ActivityList.append(item)
	context = {'ActivityList':ActivityList}
	print(context)
	return render(request, 'Olympic.html', context)

def Hstr(request):
	title=request.GET.get('title')

	mongoClient = MongoClient('research35.db',27017)
	#mongoClient = MongoClient('192.168.0.153',27017)
	DBClient = mongoClient['olympicdb']
	collection = DBClient['activitydata']
	ActivityData=collection.find_one({'title':title})
	collection = DBClient['replydata']
	result=collection.find({'title':title})
	ReplyList=[]
	for item in result:
		ReplyList.append(item)
	context = {'data':ActivityData,'ReplyList':ReplyList}
	print(context)
	return render(request, 'hstr.html', context)

def LoadPreData(request):
	mongoClient = MongoClient('research35.db',27017)
	#mongoClient = MongoClient('192.168.0.153',27017)
	DBClient = mongoClient['olympicdb']
	collection = DBClient['predata']
	result=collection.find({})
	context = {
		'title':'',
		'datetime':'',
		'content':'',
		'lcoation':'',
		}
	for item in result:
		if item['key'] == 'title':
			context['title']=item['value']
		if item['key'] == 'datetime':
			context['datetime']=item['value']
		if item['key'] == 'content':
			context['content']=item['value']
		if item['key'] == 'location':
			context['location']=item['value']
	return HttpResponse(json_util.dumps(context))

def LoadReply(request):
	title=request.POST['title']
	mongoClient = MongoClient('research35.db',27017)
	#mongoClient = MongoClient('192.168.0.153',27017)
	DBClient = mongoClient['olympicdb']
	collection = DBClient['replydata']
	result=collection.find({'title':title})
	ReplyList=[]
	for item in result:
		ReplyList.append(item)
	print(ReplyList)

	context = {'ReplyList':json_util.dumps(ReplyList)}
	return HttpResponse(context)

def Reply(request):
	user=request.POST['username']
	text=request.POST['text']
	title=request.POST['title']

	replyObj={
		'user':user,
		'text':text,
		'title':title,
	}
	print(replyObj)
	#mongoClient = MongoClient('192.168.0.153',27017)
	mongoClient = MongoClient('research35.db',27017)
	DBClient = mongoClient['olympicdb']
	collection = DBClient['replydata']
	result=collection.insert(replyObj)
	return HttpResponse("ok")
