from django.shortcuts import render
# from django.http import HttpResponse


def post_list(request):
    return render(request, 'base/post_list.html')
