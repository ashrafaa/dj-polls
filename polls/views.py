from django.http import HttpResponse

def polls(request):
    return HttpResponse("Which one you like better?")
