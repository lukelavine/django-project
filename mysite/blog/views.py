from django.shortcuts import render
from blog.models import Post

def index(request):
	posts = Post.objects.all().order_by('-published')
	context = {
		"posts": posts,
	}
	return render(request, "blog_index.html", context)

def detail(request, pk):
	post = Post.objects.get(pk=pk)
	context = {
		"post": post
	}
	return render(request, "blog_detail.html", context)