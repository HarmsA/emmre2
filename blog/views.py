from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from blog.form import ArticleForm
from blog.models import Article


def blog(request, slug):
    article = get_object_or_404(Article, slug=slug)
    print(article.title)
    context = {
        'article': article
    }
    return render(request, 'blog/blog.html', context=context)


def blogs(request):
    blogs = Article.objects.all().order_by('-date_published')
    p = Paginator(blogs, 2)
    print('Number of pages', p.num_pages)
    category_list = []
    category_list_items = []
    for blog in blogs:
        # print(category.name)
        # print(category_list)
        if blog.category.name not in category_list:
            # print(category.name)
            category_list.append(blog.category.name)
            category_list_items.append(blog)
    # for item in category_list_items:
    #     print(item)
    page_num = request.GET.get('page', 1)
    try:
        page = p.page(page_num)
    except:
        page = p.page(1)
    auth=False
    if request.user.is_authenticated:
        auth=True
    context = {
        'title': 'Emmre Blogs',
        'blogs': page,
        'first_blog_category': category_list_items,
        'auth': auth,
    }
    print('$'*80)
    return render(request, 'blog/blogs.html', context=context)


def create_post(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            title = form.cleaned_data['title']
            short_description = form.cleaned_data['short_description']
            content = form.cleaned_data['content']
            tag = form.cleaned_data['tag']
            category = form.cleaned_data['category']
            published_status = form.cleaned_data['published_status']
            visibility = form.cleaned_data['visibility']
            date_published = form.cleaned_data['date_published']
            is_featured = form.cleaned_data['is_featured']
            slug = form.cleaned_data['slug']

    else:
        form = ArticleForm()
    context = {
        'title': 'Create Blog Article',
        'form': form,
    }
    return render(request, 'blog/create-post.html', context=context)


def edit_post(request, id):
    post = Article.objects.get(id=id)
    form = ArticleForm(instance=post)
    context = {
        "post": post,
        'form': form,
    }
    return render(request, 'blog/create-post.html', context=context)


def delete_post(request, id):
    post = Article.objects.get(id=id)
    form = ArticleForm(instance=post)
    context = {
        "post": post,
        'form': form,
    }
    return render(request, 'blog/delete-post.html', context=context)


# @login_required
# class PostCreate(LoginRequiredMixin, CreateView):
#     model = Article
#     fields = '__all__'
#     success_url = reverse_lazy('blog')


# @login_required
class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Article
    fields = '__all__'
    success_url = reverse_lazy('blog')


# @login_required
class PostDelete(LoginRequiredMixin, DeleteView):
    model = Article
    success_url = reverse_lazy('blog')


