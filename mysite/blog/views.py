from django.shortcuts import render
from blog.models import Post

#give the latest
def index(request):
	post = Post.objects.latest('published')
	context = {
		"post": post,
		"prev": post.id-1,
		"next": 0
	}
	return render(request, "blog_detail.html", context)

def detail(request, pk):
	post = Post.objects.get(pk=pk)
	latest = Post.objects.latest('published')
	next = pk + 1
	if post.id == latest.id:
		next = 0
	context = {
		"post": post,
		"next": next,
		"prev": pk-1
	}
	return render(request, "blog_detail.html", context)

#TODO display all devlog post titles on one page
def all(request):
	return None