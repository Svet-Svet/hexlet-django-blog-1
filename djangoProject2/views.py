from django.shortcuts import render


def index(request):
    return render(request, 'index.html', context={
        'who': 'Denis — eto moi pervie strochki koda na Django',
    })


def about(request):
    return render(request, 'about.html')
