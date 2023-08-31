from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

# def january(request):
#     return HttpResponse("This is working very well !!!")


# def february(request):
#     return HttpResponse("this is february")

# def march(request):
#     return HttpResponse("this is march")


def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "this is january"
    elif month == "february":
        challenge_text = "this is february"
    elif month == "march":
        challenge_text = "this is march"
    else:
        return HttpResponseNotFound("this month is not available")
    return HttpResponse(challenge_text)

