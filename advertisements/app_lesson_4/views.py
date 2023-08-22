from django.shortcuts import render
from .models import Advertisement

def index(request):
    #получение списка всех объектов базы данных
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'index.html', context)

def top_sellers(request):
    return render(request, 'top-sellers.html')