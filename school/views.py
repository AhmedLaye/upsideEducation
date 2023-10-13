from tkinter.tix import STATUS
from django.shortcuts import render
import selectors
from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from . import forms
from django.contrib.auth import login, authenticate  # import des fonctions login et authenticate
from django.contrib.auth.decorators import login_required
import csv





def index(request):
    return render(request, 'index.html')


@login_required
def dash(request):
    info=Info.objects.all()
    note_dict = {}

    if request.user.is_superuser == True:
        notes = Note.objects.all().order_by('-matiere')
        devoirs=Devoir.objects.all()
        nb_devoir=devoirs.count
        discipline=Matiere.objects.all()


    else:
        notes = Note.objects.filter(eleve__username=request.user).order_by('-matiere')
        devoirs=Devoir.objects.all()
        note_dict={}
        for devoir in devoirs:
            for note in notes:
                if note.matiere==devoir.matiere:
                    try:
                        note_dict[note.matiere].append(note.valeur)
                    except:
                        note_dict[note.matiere]=[]
                        note_dict[note.matiere].append(note.valeur)

        nb_devoir=devoirs.count
        discipline=Matiere.objects.all()
        print(note_dict)
    return render(request, 'dashboard.html', 
    {'devoirs':devoirs,'nb_devoir':nb_devoir,'discipline':discipline,'info':info,'notes':notes,'note_dict':note_dict})




def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = f'Bonjour, {user.username}! Vous êtes connecté.'
                return redirect('index')
            else:
                message = 'Identifiants invalides.'
    return render(
        request, 'login.html', context={'form': form, 'message': message})



def logout_user(request):
    
    logout(request)
    return redirect('login')


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect('index')
    return render(request, 'signup.html', context={'form': form})






@login_required
def cour_upload(request):
    form = forms.CoursForm()
    if request.method == 'POST':
        form = forms.CoursForm(request.POST, request.FILES)
        if form.is_valid():
            cour = form.save(commit=False)
            # set the uploader to the user before saving the model
            Cour.uploader = request.user
            # now we can save
            cour.save()
            return redirect('home')
    return render(request, 'school/cours/cour_upload.html', context={'form': form})

@login_required
def all_devoir(request):
    devoir = Devoir.objects.filter(eleve__username=request.user)
    return render(request, 'school/devoirs/devoir.html', context={'devoir':devoir})

@login_required
def cours(request):
    cours=Cour.objects.all()
    return render(request, 'school/cours/cours.html', context={'cours':cours,})


@login_required
def coursInfo(request):
    cours=Cour.objects.all()
    return render(request, 'school/cours/cours_informatique.html', context={'cours':cours,})
    #  headers={
#     "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15",
#     "Accpet-Language":"en",
#  }
    #    # url ="https://www.education.sn"
#     # r = requests.get(url, headers = headers)
#     # soup = BeautifulSoup(r.content, 'html.parser')
#     # soup.prettify()
#     # # name=soup.find_all("div", attrs={"class": "views-field-body"})
#     # all_movies = soup.find_all(name="div", class_="views-col")
    
#     # movie_titles = [movie.getText() for movie in all_movies]
#     # movie_link = [movie.a.get('href') for movie in all_movies]
#     # movie_img=[movie.img.get('src') for movie in all_movies]
#     # mydict = {}
#     # imgnews={}
#     # for item in range(len(movie_titles)):
#     #   mydict[movie_titles[item]]=movie_link[item]
    
#     # for i in range(len(movie_titles)):
#     #   imgnews[movie_titles[i]]=movie_img[i]
#     # mydict=mydict.items() 

#     #returns : 'imgnews':imgnews, 'movie_titles':movie_titles,'movie_link':movie_link,'url':url,'movie_img':movie_img,'mydict':mydict,