from django.shortcuts import render

from blog.models import Post

# Create your views here.
def home(request):
	recent_post = Post.objects.latest('published')
	context = {'recent_post': recent_post}
	return render(request, 'home/index.html', context)
