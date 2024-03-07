from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'souls_build/index.html'
