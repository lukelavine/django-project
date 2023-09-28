from django.shortcuts import render
from portfolio.models import PortfolioEntry

# Create your views here.
def portfolio(request):
	entries = PortfolioEntry.objects.all()
	context = {
		"entries": entries
	}
	return render(request, 'portfolio.html', context)

def detail(request, pk):
	entry = PortfolioEntry.objects.get(pk=pk)
	context = {
		"entry": entry
	}
	return render(request, "portfolio_detail.html", context)