from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.template import loader
from bson.objectid import ObjectId
from bson import json_util
from pymongo import MongoClient
import time

def Index(request):
    context = {'context':'context'}
    return render(request, 'Olympic.html', context)

def HsytYY1(request):
    context = {'context':'context'}
    return render(request, 'hstr-yy1.html', context)
	
def HsytNY1(request):
    context = {'context':'context'}
    return render(request, 'hstr-nongyao1.html', context)

def LoadPreData(request):
	mongoClient = MongoClient('pr.db',27017)
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
	mongoClient = MongoClient('pr.db',27017)
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

	print("ok")
	user=request.POST['username']
	text=request.POST['text']
	title=request.POST['title']

	replyObj={
		'user':user,
		'text':text,
		'title':title,
	}

	mongoClient = MongoClient('pr.db',27017)
	DBClient = mongoClient['olympicdb']
	collection = DBClient['replydata']
	result=conf.insert(replyObj)
	print(result)
	return HttpResponse("ok")
