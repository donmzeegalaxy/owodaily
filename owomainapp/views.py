from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Newsletter, Blog
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def index(request):
    most_recent = Blog.objects.order_by('-time')[0:3]

  
    if request.method=="POST":
        if 'email' in request.POST:
            email = request.POST['email']
            new_sub = Newsletter()
            new_sub.email = email
            new_sub.save()
        else:
            email = False

    context = {
        'most_recent':most_recent,
    
    }
    return render(request, 'index.html', context)

def blog(request):
    post = Blog.objects.order_by('-time')
    paginator = Paginator(post, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)

    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)

    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    if request.method=="POST":
        if 'email' in request.POST:
            email = request.POST['email']
            new_sub = Newsletter()
            new_sub.email = email
            new_sub.save()
        else:
            email = False

    context = {
        'post':post,
       
        'page_request_var':page_request_var,
        'post': paginated_queryset,
    }
    return render(request, 'blog.html', context)

def post(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    try:
        next_post = post.get_next_by_time()
    except Blog.DoesNotExist:
        next_post = None

    try:    
        previous_post = post.get_previous_by_time()
    except Blog.DoesNotExist:
        previous_post = None

    if request.method=="POST":
        if 'email' in request.POST:
            email = request.POST['email']
            new_sub = Newsletter()
            new_sub.email = email
            new_sub.save()
        else:
            email = False


    context = {
        'previous_post':previous_post,
        'next_post':next_post,
        'post':post,
    }
    return render(request, 'post.html', context)
