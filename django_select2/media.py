from django.conf import settings
from django.templatetags.static import static

from . import __BOOTSTRAP as BOOTSTRAP

# Local version of DEBUG
DEBUG = settings.configured and settings.DEBUG


def django_select2_static(file):
    return static('django_select2/' + file)


def get_select2_js_libs():
    if DEBUG:
        js_file = 'js/select2.js'
    else:
        js_file = 'js/select2.min.js'
    return (django_select2_static(js_file), )


def get_select2_heavy_js_libs():
    libs = get_select2_js_libs()

    if DEBUG:
        js_file = 'js/heavy_data.js'
    else:
        js_file = 'js/heavy_data.min.js'
    return libs + (django_select2_static(js_file), )


def get_select2_css_libs(light=False):
    css_files = []
    if DEBUG:
        css_files = ('css/select2.css',)
    else:
        css_files = ('css/select2.min.css',)

    return map(lambda x: django_select2_static(x), css_files)
