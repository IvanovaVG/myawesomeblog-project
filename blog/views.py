from django.shortcuts import render
from .models import Blog

# Create your views here.

def showblog(request):
	print("Im here not bad!")
	blogs = Blog.objects
	return render(request, 'blog.html', {'blogs': blogs})