from django.shortcuts import render

# Create your views here.
def portfolio(request):
    return render(request, 'portfolio.html')

def contact(request):
    return render(request, 'contact.html')

def projects(request):
    return render(request, 'projects.html')