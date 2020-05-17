from collections import Counter

from django.shortcuts import render_to_response

counter_show = Counter()
counter_click = Counter()
template_original = 'landing.html'
template_test = 'landing_alternate.html'


def index(request):
    if request.GET.get('from-landing') == 'original':
        counter_click['from-landing=original'] += 1
        print('original_from', counter_click['from-landing=original'])
        return render_to_response('index.html')
    elif request.GET.get('from-landing') == 'test':
        counter_click['from-landing=test'] += 1
        print('test_from', counter_click['from-landing=test'])
        return render_to_response('index.html')
    else:
        return render_to_response('index.html')


def landing(request):
    if request.GET['ab-test-arg'] == 'original':
        counter_show['ab-test-arg=original'] += 1
        print('a-b_original', counter_show['ab-test-arg=original'])
        return render_to_response('landing.html', context={'some_counter': counter_click[template_original]})
    else:
        counter_show['ab-test-arg=test'] += 1
        print('a-b_test', counter_show['ab-test-arg=test'])
        return render_to_response('landing_alternate.html', context={'some_counter': counter_click[template_test]})


def stats(request):
    if counter_show['ab-test-arg=original'] == 0 and counter_click['from-landing=original'] == 0:
        original = 0
    else:
        original = counter_click['from-landing=original'] / counter_show['ab-test-arg=original']
    if counter_click['from-landing=test'] == 0 and counter_click['ab-test-arg=test'] == 0:
        test = 0
    else:
        test = counter_show['ab-test-arg=test'] / counter_click['from-landing=test']
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
