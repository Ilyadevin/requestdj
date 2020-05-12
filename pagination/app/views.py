from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import csv


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    stations_info = list()
    with open('data-398-2018-08-30.csv', 'r', encoding='cp1251') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            stations_info.append({'Name': [row['StationName'], ], 'Street': [row['Street'], ],
                                  'District': [row['District'], ]})
    for q in stations_info:
        all_objects = q.all('Name')
        paginator = Paginator(all_objects, 10)
        next_page_url = request.GET.get('page')
        try:
            all_objects = paginator.page(next_page_url)
        except PageNotAnInteger:
            all_objects = paginator.page(1)
        except EmptyPage:
            all_objects = paginator.page(paginator.num_pages)
        return render_to_response('index.html', context={
            'bus_stations': stations_info,
            'current_page': all_objects,
            'prev_page_url': None,
            'next_page_url': all_objects,
        })
