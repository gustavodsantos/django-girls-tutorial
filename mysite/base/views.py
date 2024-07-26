from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from mysite.base.models import Post


# from django.http import HttpResponse


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'base/post_list.html', {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'base/post_detail.html', {"post": post})
