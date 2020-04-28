from collections import Counter

from django.shortcuts import render_to_response

counter_show = Counter()
counter_click = Counter()
template_original = 'landing.html'
template_test = 'app/landing_alternate.html'


def index(request):
    global counter_show, counter_click
    if 'from-landing' in request.GET['from-landing']:
        counter_show['from-landing'] += 1
        counter_click['from-landing'] += 1
    else:
        pass
    return render_to_response('index.html')


def landing(request):
    global counter_show, counter_click

    if 'ab-test-arg' in request.GET['app/landing_alternate.html' or template_original]:
        counter_show[template_test] += 1
        counter_click[template_test] += 1
    else:
        counter_click[template_original] += 1
        counter_show[template_original] += 1
    return render_to_response(template_original, template_test)


def stats(request):
    original = counter_click[template_original] / counter_show[template_original]
    test = counter_click[template_test] / counter_show[template_test]
    if original or test in request.GET('marker'):
        return render_to_response('stats.html', context={
            'test_conversion': 0.5,
            'original_conversion': 0.4,
        })
