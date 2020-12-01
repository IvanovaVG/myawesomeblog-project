from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404
# Create your views here.

def showblog(request):
	print("Im here not bad!")
	blogs = Post.objects
	return render(request, 'post/blog.html', {'blogs': blogs})

def post_details(request, post_id):
	blog = get_object_or_404(Post, pk=post_id)
	return render(request, 'post/post_details.html', {'blog':blog})