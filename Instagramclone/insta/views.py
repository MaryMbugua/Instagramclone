from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .forms import NewProfileForm,NewPhotoForm
from .models import Profile,Photo



# Create your views here.
def landing(request):
    current_user = request.user
    form = NewPhotoForm(request.POST,request.FILES)
    if request.method == 'POST': 
        if form.is_valid():
            photo = form.save(commit=False)
            photo.person = current_user
            photo.save()
    else:
        form = NewPhotoForm()

    images = Photo.objects.all()
    
    return render(request,'index.html',{"form":form,"images":images})
    
@login_required(login_url='/accounts/login/')   
def profile(request, profile_id):
    profile = Profile.objects.get(id = profile_id)
    
    form = NewPhotoForm(request.POST,request.FILES)
    if request.method == 'POST': 
        if form.is_valid():
            photo = form.save(commit=False)
            photo.person = current_user
            photo.save()
    else:
        form = NewPhotoForm()

    photos = Photo.objects.filter(person=request.user)
    
    return render(request,'profile.html',{"profile":profile,"form":form,"photos":photos})

    
@login_required(login_url='/accounts/login/')   
def edit(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.person = current_user
            profile.save()
    else:
        form = NewProfileForm()

    return render(request,'profileedit.html',{"form": form})
@login_required(login_url='/accounts/login/')   
def search(request):
    

    return render(request,'search.html')