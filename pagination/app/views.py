from django.shortcuts import render_to_response, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    with open('data-398-2018-08-30.csv', 'r', encoding='utf8') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            current_page = 1
            next_page_url = 'write your url'
            return render_to_response('index.html', context={
                'bus_stations': [{'Name': row['StationName'], 'Street': row['Street'], 'District': row['District']}],
                'current_page': current_page,
                'prev_page_url': None,
                'next_page_url': next_page_url,
            })
