from django.shortcuts import render


def index(request):
    template = "index/index.html"
    context = {}
    return render(request, template, context)
