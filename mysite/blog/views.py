from django.shortcuts import render
from blog.models import Post

#this is bad practice and should probably be handled by js instead
#it works, but when a user refreshes it asks about form resubmission
def index(request):
	selected = ""
	if request.method == "POST":
		if request.POST.get('search') != None:
			posts = Post.objects.filter(text__icontains=request.POST.get('search'))
		elif request.POST.get('sort') == 'date_a':
			posts = Post.objects.all().order_by('published')
			selected = "date_a"
		elif request.POST.get('sort') == 'alpha_d':
			posts = Post.objects.all().order_by('title')
			selected = "alpha_d"
		elif request.POST.get('sort') == 'alpha_a':
			posts = Post.objects.all().order_by('-title')
			selected = "alpha_a"
		else:
			posts = Post.objects.all().order_by('-published')
	else:
		posts = Post.objects.all().order_by('-published')
	context = {
		"posts": posts,
		"selected": selected
	}
	return render(request, "blog_index.html", context)

def detail(request, pk):
	post = Post.objects.get(pk=pk)
	context = {
		"post": post
	}
	return render(request, "blog_detail.html", context)