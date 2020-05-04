from collections import Counter

from django.shortcuts import render_to_response

counter_show = Counter()
counter_click = Counter()
template_original = 'landing.html'
template_test = 'app/landing_alternate.html'


def index(request):
    if 'from-landing' in request.GET['from-landing']:
        counter_show['from-landing'] += 1
    else:
        pass
    return render_to_response('index.html')


def landing(request):
    if 'ab-test-arg' in request.GET['app/landing_alternate.html']:
        counter_click[template_test] += 1
    else:
        counter_click[template_original] += 1
    return render_to_response(template_original, template_test)


def stats(request):
    original = counter_click[template_original] / counter_show[template_original]
    test = counter_click[template_test] / counter_show[template_test]
    if original or test != 0:
        return render_to_response('stats.html', context={
            'test': test,
            'original': original,
        })
    else:
        return render_to_response('stats.html', context={'text':
                                                             'Нет переходов',
                                                         }
                                  )
