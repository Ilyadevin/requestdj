from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import csv


def index(request):
    return redirect('index.html', reverse(bus_stations))


def bus_stations(request):
    with open('pagination/data-398-2018-08-30.csv', 'r', encoding='cp1251') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            current_page = 1
            all_objects = row.objects.all()
            paginator = Paginator(all_objects, 10)
            next_page_url = request.GET.get('page')
            stations_info = {}
            try:
                list_of_stations = paginator.page(next_page_url)
            except PageNotAnInteger:
                list_of_stations = paginator.page(1)
            except EmptyPage:
                list_of_stations = paginator.page(paginator.num_pages)
            return render_to_response('index.html', context={
                'bus_stations': stations_info.update({'Name': row['StationName'], 'Street': row['Street'], 'District': row['District']}),
                'current_page': current_page,
                'prev_page_url': None,
                'next_page_url': list_of_stations,
            })
