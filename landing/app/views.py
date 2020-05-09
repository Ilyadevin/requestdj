from collections import Counter

from django.shortcuts import render_to_response

counter_show = Counter()
counter_click = Counter()
template_original = 'landing.html'
template_test = 'app/landing_alternate.html'


def index(request):
    counter_show[request.GET['from-landing']] += 1
    return render_to_response('index.html')


def landing(request):
    if request.GET['ab-test-arg']:
        counter_click[template_test] += 1
        return render_to_response(template_test)
    elif not request.GET['ab-test-arg']:
        counter_click[template_original] += 1
        return render_to_response(template_original)
    else:
        pass


def stats(request):
    global test, original
    try:
        original = counter_click[template_original] / counter_show[template_original]
        test = counter_click[template_test] / counter_show[template_test]
    except ZeroDivisionError as error:
        if error is ZeroDivisionError:
            return render_to_response('stats.html', context={'text': 'Нет переходов',
                                                             }
                                      )
        else:
            return render_to_response('stats.html', context={
                'test': test,
                'original': original,
            })
