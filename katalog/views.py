from multiprocessing import context
from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_katalog_barang = CatalogItem.objects.all()
    context = {
        'list_barang': data_katalog_barang,
        'nama': 'Bimo',
        'student_id': '2106752395'
    }
    return render(request, "katalog.html", context)
