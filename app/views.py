from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from app.models import CustomUser
from .forms import ProfileForm
from .models import Profile,Movie,Video,CustomUser

def Home(request):
    if request.user.is_authenticated:
        return redirect('profile/')
    return render(request,'index.html')



@login_required(login_url='/accounts/login/')
def ProfileList(request):
    profile = request.user.profile.all()
    return render(request, 'profileList.html', {'profiles': profile} )

@login_required(login_url='account/login/')
def ProfileCreate(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            p =form.save()
            if p:
                request.user.profile.add(p)
                return redirect(reverse('profile'))
            
    else:
        form = ProfileForm()
        return render(request,'profileCreate.html',{'form': form})
    
@login_required(login_url='account/login/')
def Watch(request,profile_id):
    try:
        profile = Profile.objects.get(uuid=profile_id)
        movies = Movie.objects.filter(age_limit=profile.age_limit)

        if profile not in request.user.profile.all():
            return redirect('profile/')
        return render(request,'movieList.html',{'movies':movies})
    except Profile.DoesNotExist:
        return redirect('profile/')

@login_required(login_url='account/login/')
def ShowMovieDetail(request,movie_id):
    try:
        movie = Movie.objects.get(uuid=movie_id)
        return render(request,'movieDetail.html',{'movie':movie})
    except Movie.DoesNotExist:
        return redirect('profile/')

@login_required(login_url='account/login/')
def ShowMovie(request,movie_id):
    try:
        movie = Movie.objects.get(uuid=movie_id)
        movie = movie.video.values()
        return render(request,'showMovie.html',{'movie':list(movie)})

    except Movie.DoesNotExist:
        return redirect('profile/')

        
 