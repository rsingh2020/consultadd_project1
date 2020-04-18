from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'firstapp/index.html')

def training_domain(request,domain_id):
    return HttpResponse("You are in the %s:" % domain_id)

def candidate(request,domain_id):
    response = "You are the candidate named as %s."
    return HttpResponse(response % domain_id)



