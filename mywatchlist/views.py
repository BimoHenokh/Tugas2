from mywatchlist.models import MyWatchlistItem
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers

def show_html(request):
    data = MyWatchlistItem.objects.all()
    context = {
        'list_data': data,
        'nama': 'Bimo Henokh Barata'
    }
    return render(request, "mywatchlist.html", context)

def show_json(request):
    data = MyWatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml(request):
    data = MyWatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")