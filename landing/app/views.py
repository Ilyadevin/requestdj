from collections import Counter

from django.shortcuts import render_to_response

counter_show = Counter()
counter_click = Counter()


def index(request):
    global counter_show
    if 'from-landing' in request.GET['from-landing']:
        counter_show['from-landing'] += 1
        counter_click['from-landing'] += 1
    else:
        pass
    return render_to_response('index.html'), counter_click, counter_show


def landing(request):
    template_original = None
    template_test = None
    if 'ab-test-arg' in request.GET['app/landing_alternate.html' or template_original]:
        template_test = 'app/landing_alternate.html'
        template_original = 'landing.html'
        counter_show[template_test] += 1
        counter_click['ab-test-arg'] += 1
    return render_to_response(template_original, template_test), counter_click, counter_show


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    return render_to_response('stats.html', context={
        'test_conversion': 0.5,
        'original_conversion': 0.4,
    })
