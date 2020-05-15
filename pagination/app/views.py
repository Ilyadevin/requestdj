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
            stations_info.append({'Name': f"{row['StationName']}, {row['Direction']}", 'Street': row['Street'],
                                  'District': row['District']})
    paginator = Paginator(stations_info, 15)
    print(paginator.count)
    current_page = request.GET.get('page', 1)
    try:
        stations = paginator.get_page(current_page)
    except PageNotAnInteger:
        stations = paginator.page(number=1)
    except EmptyPage:
        stations = paginator.page(paginator.num_pages)
    prev_page, next_page = None, None
    if stations.has_previous():
        prev_page = stations.previous_page_number()
    elif stations.has_next():
        next_page = stations.next_page_number()
    context = {
        'bus_stations': stations,
        'current_page': current_page,
        'prev_page_url': prev_page,
        'next_page_url': next_page,
    }
    return render_to_response('index.html', context=context)
