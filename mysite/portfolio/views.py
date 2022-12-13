from django.shortcuts import render
from portfolio.models import PortfolioEntry

# Create your views here.
def portfolio(request):
	entries = PortfolioEntry.objects.all()
	context = {
		"entries": entries
	}
	return render(request, 'portfolio.html', context)