from django.shortcuts import render
from .models import Post

# Create your views here.

def showblog(request):
	print("Im here not bad!")
	blogs = Post.objects
	return render(request, 'post/blog.html', {'blogs': blogs})
