from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.utils.translation import get_language, activate, gettext
from django.views.generic import DetailView, RedirectView


def translate(lang):
    current_lang = get_language()
    try:
        activate(lang)
        text = gettext('hello')
    finally:
        activate(current_lang)
    return text


def home(request):
    trans = translate(lang='ja')
    return render(request, 'pages/home.html', {'trans': trans})
