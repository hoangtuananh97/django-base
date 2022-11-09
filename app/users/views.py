from django.shortcuts import render
from django.utils.translation import activate, get_language, gettext


def translate(lang):
    current_lang = get_language()
    try:
        activate(lang)
        text = gettext("hello")
    finally:
        activate(current_lang)
    return text


def home(request):
    trans = translate(lang="ja")
    return render(request, "pages/home.html", {"trans": trans})
