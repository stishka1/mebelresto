from django.shortcuts import render, get_object_or_404, HttpResponse
from main.models import *
from taggit.models import Tag 
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string
from django.core import serializers
from .forms import PostForm, TagForm
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Q



def index(request, tag_slug=None, page_number = 1):
    posts = Post.objects.all()
    per_page = 2
    paginator = Paginator(posts, per_page)
    products_paginator = paginator.page(page_number)
    # Выборка постов по тегам
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug, id=9)
        posts = posts.filter(tags__in=[tag])
    context = {
        'posts': products_paginator,
        }
    return render(request, 'main/index.html', context)



def detail(request, slug):
    # slug=slug
    post = get_object_or_404(Post, slug=slug)

    # Выборка постов по тегам
    # tag = None
    # if tag_slug:
    #     tag = get_object_or_404(Tag, slug=tag_slug)
    #     posts = posts.filter(tags__in=[tag])
    context = {
        'post': post,
        }
    return render(request, 'main/detail.html', context)


def live_search(request):
    if request.accepts("application/json"):
        res = None
        post = request.POST.get('post')
        qs = Post.objects.filter(tags__name__icontains = post).distinct()[:5]
        if len(qs) > 0 and len(post) > 0:
            lst = []
            for i in qs:
                item = {
                    'pk': i.pk,
                    'slug': i.slug,
                    'title': i.title,
                    'image': str(i.preview_img.url)
                    }
                lst.append(item)
            res = lst
        else:
            res = 'Нет постов с такими тегами...'
        return JsonResponse({'data': res})
    return JsonResponse({})

def search(request):
    query = request.GET.get('q')
    posts = Post.objects.filter(
            Q(tags__name__icontains = query)
            ).distinct()
    context = {
        'posts': posts,
        }

    return render(request, 'main/search_results.html', context)



def services(request):
    return render(request, 'main/services.html')


def about(request):
        data = {
            }
        return render(request, 'main/about.html', data)


def post_modal(request, id):
    # data = get_object_or_404(Post, id=id)
    data = Post.objects.filter(id=id) # get метод идет в str сначала (Models)
    # d = render_to_string('main/index.html', {'data': data.title})
    # print(data)
    # d, lst = {}, []
    # for i in data:
    #     d['title'] = i.title
    #     d['description'] = i.description
    # print(d)
    posts_serialized = serializers.serialize('json', data)
    return JsonResponse(json.dumps(posts_serialized, ensure_ascii=False), safe=False)
        # posts_serialized, safe=False
    # t=render_to_string('main/index.html',{'data':posts_serialized})
    # return JsonResponse({'data':t})
    # return JsonResponse(data)


# Отображение постов со схожими тегами
def tag_list(request, tag_slug=None):
    posts = Post.objects.all()

    # Выборка постов по тегам
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    context = {
        'posts': posts,
    }
    return render(request, 'main/tag_list.html', context)

@csrf_exempt
def add_url(request):
    date = request.POST.get('id')
    print(date)
    return render(request, 'main/p.html')