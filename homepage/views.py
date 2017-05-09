from django.template.response import TemplateResponse


def index(request):
    context = {
        'page_title': 'HOME PAGE'

    }
    return TemplateResponse(request, 'index.html', {})


def contacts(request):
    context = {
        'page_title': 'Contact Me'
    }
    return TemplateResponse(request, 'contact.html', {})
