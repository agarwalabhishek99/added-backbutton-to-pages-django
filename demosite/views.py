from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Home page</h1>")

def page1(request):
    return HttpResponse("page1 <a href='/'> Back </a>")

def page2(request):
    return HttpResponse("page2 <a href='/'> Back </a>")

def page3(request):
    return HttpResponse("page3 <a href='/'> Back </a>")

def page4(request):
    return HttpResponse("page4 <a href='/'> Back </a>")

def page5(request):
    return HttpResponse("page5 <a href='/'> Back </a>")