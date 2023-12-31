from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse 
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


# classes = {
#     "maths": "this is math",
#     "english": "this is english",
#     "biology": "this is biology"
# }


# def lectures_by_number(request, module):
#     modules = list(classes.keys())

#     if module > len(modules):
#         return HttpResponseNotFound("invalid module")
    
#     redirect_module = modules[module - 1]
#     redirect_path = reverse("month-challenge", args =[redirect_module])
#     return HttpResponseRedirect(redirect_path)


# def lectures(request, module):
#     try:
#         modules = classes[module]
#         return HttpResponse(modules)
#     except:
#         return HttpResponseNotFound("modules not found")
    


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("invalid month")
    
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args = [redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("this month is not available")
