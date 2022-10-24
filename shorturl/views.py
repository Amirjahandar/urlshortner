from django.shortcuts import render
from django.http import HttpResponse
from .models import ShortUrl
from .forms import CreateNewShortUrl
from datetime import datetime
import random, string


def home(request):
    return render(request, 'home.html')


def createshorturl(request):
    if request.method == 'POST':
        form = CreateNewShortUrl(request.POST)
        if form.is_valid():
            originalurl = form.cleaned_data['original_url']
            random_chars_list = list(string.ascii_letters)
            random_chars = ''
            for i in range(6):
                random_chars += random.choice(random_chars_list)
            while len(ShortUrl.objects.filter(short_url=random_chars)) != 0:
                for i in range(6):
                    random_chars += random.choice(random_chars_list)
            d = datetime.now()
            s = ShortUrl(original_url=originalurl, short_url=random_chars, time_date_created=d)
            s.save()
            return render(request, 'urlcreated.html', {'chars':random_chars})

    else:
        form = CreateNewShortUrl()
        return render(request, 'create.html',{'form':form})







def redirect_url(request, url:str):
    try:
        current_obj = ShortUrl.objects.get(short_url=url)
        context = {'obj':current_obj}
        return render(request, 'redirect.html', context)
    except:
        return render(request, 'pagenotfound.html')


