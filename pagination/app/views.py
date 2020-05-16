from django.shortcuts import redirect, render
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    stations_info = list()
    with open('data-398-2018-08-30.csv', 'r', encoding='cp1251') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            stations_info.append({'Name': f"{row['StationName']}, {row['Street']} ({row['Direction']})",
                                  'Street': row['Street'], 'District': row['District']})
    paginator = Paginator(stations_info, 15)
    current_page = request.GET.get('page', 1)
    stations = paginator.get_page(current_page)
    next_page, prev_page = None, None
    if stations.has_next():
        next_page = stations.next_page_number()
    if stations.has_previous():
        prev_page = stations.previous_page_number()
    context = {
        'bus_stations': stations,
        'current_page': current_page,
        'prev_page_url': f'?page_prev={prev_page}',
        'next_page_url': f'?page={next_page}',
    }
    return render(request, 'index.html', context=context)
