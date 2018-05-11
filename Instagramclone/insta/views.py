from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect



# Create your views here.
def landing(request):
    
    return render(request,'index.html')
    
def profile(request):

    return render(request,'profile.html')