from collections import Counter

from django.shortcuts import render_to_response

counter_show = Counter()
counter_click = Counter()
template_original = 'landing.html'
template_test = 'app/landing_alternate.html'


def index(request):
    if 'from-landing' in request.GET:
        request.GET.click()
        counter_show['from-landing'] += 1
        return render_to_response('index.html')
    else:
        return render_to_response('index.html')


def landing(request):
    if request.GET['ab-test-arg']:
        counter_click[template_test] += 1
        return render_to_response('app/landing_alternate.html', context={'some_counter': counter_click[template_test]})
    elif not request.GET['ab-test-arg']:
        counter_click[template_original] += 1
        return render_to_response('landing.html', context={'some_counter': counter_click[template_original]})
    return render_to_response('landing.html', 'app/landing_alternate.html', )


def stats(request):
    original = counter_click[template_original] / counter_show[template_original]
    test = counter_click[template_test] / counter_show[template_test]
    if original == ZeroDivisionError:
        return render_to_response('stats.html', context={'text': f'Original - {ZeroDivisionError} - Нет переходов',
                                                         }
                                  )
    elif test == ZeroDivisionError:
        return render_to_response('stats.html', context={'text': f'Test - {ZeroDivisionError} - Нет переходов',
                                                         }
                                  )
    else:
        return render_to_response('stats.html', context={'test': test,
                                                         'original': original,
                                                         }
                                  )
