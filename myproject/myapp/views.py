from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    context={
        'name':'Patrick',
        'age':37,
        "Nationality":"British"}
    return render(request, 'index.html', context)

def counter(request):
    words=request.GET['text']
    total= len(words.split())
    return render(request,'counter.html',{'amount':total})
