from django.shortcuts import render, redirect
from django.views.generic import ListView

from .forms import UserRegistrationForm, NewAdForm
from .models import NewAd
from .filters import CarFilter


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
            return render(request, 'main/login.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'main/registration.html', {'form': user_form})


def login(request):
    return render(request, 'main/login.html')


def ads(request):
    ads = NewAd.objects.all()

    myFilter = CarFilter(request.GET, queryset=ads)
    ads = myFilter.qs

    return render(request, 'main/ads.html', {'ads': ads, 'myFilter':myFilter})


def newad(request):
    userid = request.user.id
    error = ''
    if request.method == 'POST':
        form = NewAdForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user_name = request.user.first_name
            form.user_id = request.user.id
            form.save()
        else:
            error = 'Данные введены некорректно'
    form = NewAdForm()

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


def ad(request):
    adId = request.GET.get("id", False)
    ad = NewAd.objects.get(pk=adId)
    if len(ad.user_name) == 0:
        ad.user_name = "Не вказано"
    priceuah = float(ad.price) * 29.5
    priceeur = float(ad.price) * 0.9
    context = {
        'adId': adId,
        'ad': ad,
        'priceuah': int(priceuah),
        'priceeur': int(priceeur),
    }
    return render(request, 'main/ad.html', context)




