import datetime

from django.shortcuts import render
from django.utils import timezone

from blog.models import Post
from .models import Contact

# Create your views here.
def home(request):
	if request.method=='POST':
		p = Contact(timesent=datetime.datetime.now(), name=request.POST['name'], subject=request.POST['subject'], email=request.POST['email'], message=request.POST['message'])
		p.save()
	recent_post = Post.objects.latest('published')
	context = {'recent_post': recent_post}
	return render(request, 'home/index.html', context)
