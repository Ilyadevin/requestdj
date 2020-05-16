from collections import Counter

from django.shortcuts import render_to_response

counter_show = Counter()
counter_click = Counter()
template_original = 'landing.html'
template_test = 'landing_alternate.html'


def index(request):
    if request.GET['from-landing'] == 'original':
        counter_show['from-landing=original'] += 1
        return render_to_response('index.html')
    else:
        counter_show['from-landing=test'] += 1
        return render_to_response('index.html')


def landing(request):
    if request.GET['ab-test-arg'] == 'original':
        counter_click[template_original] += 1
        return render_to_response('landing.html', context={'some_counter': counter_click[template_original]})
    else:
        counter_click[template_test] += 1
        return render_to_response('landing_alternate.html', context={'some_counter': counter_click[template_test]})


def stats(request):
    try:
        original = counter_click[template_original] / counter_show[template_original]
    except ZeroDivisionError as zero_error:
        original = 1
    try:
        test = counter_click[template_test] / counter_show[template_test]
    except ZeroDivisionError as zero_error:
        test = 1
    if original == 0 and test == 0 in request.GET:
        return render_to_response('stats.html', context={
            'original_conversion': f'original_conversion - {ZeroDivisionError} - Нет переходов',
            'test_conversion': f'test_conversion - {ZeroDivisionError} - Нет переходов',
        }
                                  )
    else:
        return render_to_response('stats.html', context={'test_conversion': test,
                                                         'original_conversion': original,
                                                         }
                                  )
