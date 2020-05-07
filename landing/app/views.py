from collections import Counter

from django.shortcuts import render_to_response

counter_show = Counter()
counter_click = Counter()
template_original = 'landing.html'
template_test = 'app/landing_alternate.html'


# Александр, здравствуйте, забыл написать в сообщении коммент.
# с возвращением шаблонов - мне в данном случае нужно возвращать два шаблона "test" & "original"?
def index(request):
    if 'from-landing' in request.GET:
        counter_show['from-landing'] += 1
        return render_to_response(template_original)
    elif 'from-landing' not in request.GET:
        return render_to_response(template_test)
    else:
        pass
    return render_to_response('index.html')


def landing(request):
    if 'ab-test-arg' in request.GET:
        ab_test = request.GET['app/landing_alternate.html']
        counter_click[template_test] += 1
    else:
        counter_click[template_original] += 1
    return render_to_response(template_original, template_test)


# Правильно ли я поступил с переменными в методе stats?
def stats(request):
    global test, original
    try:
        original = counter_click[template_original] / counter_show[template_original]
        test = counter_click[template_test] / counter_show[template_test]
    except ZeroDivisionError as error:
        if error is True:
            return render_to_response('stats.html', context={'text': 'Нет переходов',
                                                             }
                                      )
        else:
            return render_to_response('stats.html', context={
                'test': test,
                'original': original,
            })
