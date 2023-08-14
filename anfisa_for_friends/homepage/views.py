from django.shortcuts import render

from ice_cream.models import IceCream


def index(request):
    template = 'homepage/index.html'
    iice_cream_list = IceCream.objects.values('id', 'title', 'description').filter(is_published=True, is_on_main=True).order_by('title').values('id', 'title', 'description')[:3]
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template, context)

