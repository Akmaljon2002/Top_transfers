from django.shortcuts import render
from .models import *
from django.db.models import Sum, F
from django.db.models.functions import Abs

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

# 2
def clubs(request):
    data = {
        'clublar':Club.objects.annotate(umum_summa=Sum('futbolchilari__tr_narxi')).\
            order_by('-umum_summa')
    }
    return render(request, 'clubs.html', data)


def players(request):
    data = {
        'players':Player.objects.order_by("-tr_narxi").all()
    }
    return render(request, 'players.html', data)

# 1

def latest_tarnsfers(request):
    data = {
        'l_transfers':Transfer.objects.filter(mavsum=Hozirgi_mavsum.objects.all()[0]).order_by('-narxi')
    }
    return render(request, 'latest-transfers.html', data)


# 3
def tr_records(request):
    data = {
        "tr_records":Transfer.objects.filter(narxi__gt=50).order_by("-narxi")[:100]
    }
    return render(request, 'stats/transfer-records.html', data)



def u_20_players(request):
    from datetime import date, timedelta
    bugun = date.today()
    boshi = bugun - timedelta(days=7295)
    player = Player.objects.filter(t_yil__range=[boshi, bugun])
    data = {
        'u_players':player,
        'h_yil':bugun.year
    }
    return render(request, 'U-20 players.html', data)


# 1
def club(request, son):
    data = {
        'club':Club.objects.get(id=son),
        'c_players':Player.objects.filter(club_id=son).order_by('-tr_narxi')
    }
    return render(request, 'country-clubs.html', data)



def transfers_m(request, m):
    data = {
        'm_transfers':Transfer.objects.filter(mavsum=m),
        "mavsum":m
    }
    return render(request, '2017-18season.html', data)

# 4

def countries(request, country):
    data = {
        'c_clubs':Club.objects.filter(davlat=country),
        'davlat':country
    }
    return render(request, 'england.html', data)


def tryouts(request):
    return render(request, 'tryouts.html')

def stats(request):
    return render(request, 'stats.html')

def transfer_archive(request):
    h_mavsum = Hozirgi_mavsum.objects.first().hozirgi_mavsum
    data = {
        'archive':Transfer.objects.filter(mavsum__lt=h_mavsum).values('mavsum').distinct().order_by('mavsum')
    }
    return render(request, 'transfer-archive.html', data)

def accurate_predictions(request):
    result = Transfer.objects.annotate(difference=Abs(F('narxi')-F('tax_narx')))

    result = result.annotate(divergence=100*F('difference')/F('narxi')).order_by('divergence')

    data = {
        "accurate_pr":result
    }
    return render(request, "stats/150-accurate-predictions.html", data)
