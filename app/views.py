from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required

def Home(request):
    if request.user.is_authenticated:
        return redirect('profile/')
    return render(request,'index.html')



@login_required(login_url='/accounts/login/')
def ProfileList(request):
    profiles = request.user.profile.all()
    return render(request, 'profileList.html', {'profiles': profiles})


def ProfileCreate(request):
    return render(request,'profileCreate.html')