from django.contrib import admin
from django.urls import path
from asosiy.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', about),
    path('clubs/', clubs),
    path('players/', players),
    path('tryouts/', tryouts),
    path('stats/', stats),
    path('latest-transfers/', latest_tarnsfers),
    path('u-20-players/', u_20_players),
    path('stats/transfer-records/', tr_records),
    path('stats/150-accurate-predictions/', accurate_predictions),
    path('transfer-archive/', transfer_archive),

    ####################################################################################################################
    path('club/<int:son>/', club),
    path('countries/<str:country>/', countries),
    path('transfer/<str:m>/', transfers_m),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
