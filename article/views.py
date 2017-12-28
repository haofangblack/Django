# encoding=utf-8
from django.shortcuts import render#xuanran template
from django.http import HttpResponse
from article.models import Article
from datetime import datetime


def add(request):
	a = request.GET['a']
	b = request.GET['b']
	c = int(a) + int(b)
	return HttpResponse(str(c))


def add1(request, a, b):
	c = int(a) + int(b)
	return HttpResponse(str(c))


def index(request):
	return render(request, 'home.html')


def detail(request, my_args):
	post = Article.objects.all()[int(my_args)]
	str = ('title=%s, category=%s, date_time=%s, content=%s' % (post.title, post.category, post.date_time, post.content))
	return HttpResponse(str)


def test(request):
	return render(request, 'test1.html', {'current_time': datetime.now()})


def home(request):
	post_list = Article.objects.all()
	return render(request, 'home.html', {'post_list': post_list})






