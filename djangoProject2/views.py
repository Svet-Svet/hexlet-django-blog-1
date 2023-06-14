from django.shortcuts import render
from django.views.generic.base import TemplateView


def about(request):
    return render(request, 'about.html')


class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'Denis — eto moi pervie strochki koda na Django'
        return context
