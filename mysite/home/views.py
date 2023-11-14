import datetime

from django.shortcuts import render
from django.utils import timezone

from blog.models import Post
from portfolio.models import PortfolioEntry

# Create your views here.
def home(request):
	recent_post = Post.objects.latest('published')
	project1 = PortfolioEntry.objects.get(pk=3)
	project2 = PortfolioEntry.objects.get(pk=2)
	context = {'recent_post': recent_post,
				'project1': project1,
				'project2': project2}
	return render(request, 'home/index.html', context)
