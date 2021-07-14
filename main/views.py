from django.http import Http404

from blog.models import Article
from .models import *
from django.shortcuts import render, get_object_or_404


# from django.views.decorators.http import require_safe
# from django.core.paginator import Paginator
# from datetime import datetime, date
# from collections import OrderedDict
# from pprint import pprint
# from ordered_set import OrderedSet
# from config.models import Setting as AdminSettings
# # from .context_processors import conference_page_info
# from .context_processors import what_site
# from .forms import BlogForm
# from django.shortcuts import get_object_or_404


def home(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'main/home.html', context=context)


def product(request):
    price_plans = PricePlan.objects.all()

    context = {
        'plans': price_plans,
        'title': "Product Plans"
    }
    return render(request, 'main/product.html', context=context)


# def newsletter(request):
#     context = {
#
#     }
#     return render(request, 'main/newsletter.html', context=context)
#


def faq(request):
    # questions = FAQ.objects.all()
    context = {
        'title': 'FAQ',
    }
    return render(request, 'main/faq.html', context=context)


def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'main/about.html', context=context)

