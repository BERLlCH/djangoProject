from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, NewAdForm
from .models import NewAd


def index(request):
    return render(request, 'main/index.html')


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'main/register_ok.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'main/registration.html', {'form': user_form})


def login(request):
    return render(request, 'main/login.html')


def ads(request):
    ads = NewAd.objects.all()
    return render(request, 'main/ads.html', {'ads': ads})


def newad(request):
    error = ''
    if request.method == 'POST':
        form = NewAdForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            redirect('ads')
        else:
            error = 'Данные введены некорректно'
    form = NewAdForm()
    userid = request.user.id
    context = {
        'form': form,
        'error': error,
        'userid': userid
    }
    return render(request, 'main/newAd.html', context)


def myads(request):
    ads = NewAd.objects.all()
    userid = str(request.user.id)

    return render(request, 'main/myAds.html', {'ads': ads, 'userid': userid})


