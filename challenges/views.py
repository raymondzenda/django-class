from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

# def january(request):
#     return HttpResponse("This is working very well !!!")


# def february(request):
#     return HttpResponse("this is february")

# def march(request):
#     return HttpResponse("this is march")


# def monthly_challenge(request, month):
#     challenge_text = None
#     if month == "january":
#         challenge_text = "this is january"
#     elif month == "february":
#         challenge_text = "this is february"
#     elif month == "march":
#         challenge_text = "this is march"
#     else:
#         return HttpResponseNotFound("this month is not available")
#     return HttpResponse(challenge_text)

monthly_challenges = {
    "january": "this is january",
    "february": "this is february",
    "march": "this is march",
    "april": "this is april",
    "may": "this is may",
    "june": "this is june",
    "july": "this is july",
    "august": "this is august",
    "september": "this is september",
    "october": "this is october",
    "november": "this is november",
    "december": "this is december"
}


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("this month is not available")

    
    


