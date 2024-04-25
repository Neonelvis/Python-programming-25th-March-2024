from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect


monthly_challenges = {
    "january": "Eat No Meat For The Entire Month",
    "february": "Hit the gym for at least 15 days",
    "march": "Save money till ksh 15000 ",
    "april": "Adopt a new productive hobby",
    "may": "Eat No Meat For The Entire Month",
    "june": "Hit the gym for at least 15 days",
    "july": "Save money till ksh 15000 ",
    "august": "Adopt a new productive hobby",
    "september": "Eat No Meat For The Entire Month",
    "october": "Hit the gym for at least 15 days",
    "november": "Save money till ksh 15000 ",
    "december": "Adopt a new productive hobby",
}

def monthly_challenge_by_number(request, month):
    # return HttpResponse(month)
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month - 1]
    return HttpResponseRedirect('/challenges/' + redirect_month)

# Create your views here.
# def january(request):
#     return HttpResponse("Eat No Meat For The Entire Month")

# def february(request):
#     return HttpResponse("Hit the gym for at least 15 days") 

# def march(requet):
#     return HttpResponse("Save money till ksh 15000 ")

# def april(request):
#     return HttpResponse("Adopt a new productive hobby")

def monthly_challenge(request, month):
#     challenge_text = None
#     if month == 'january':
#         challenge_text = "Eat No Meat For The Entire Month"
#     elif month == 'february':
#         challenge_text = "Hit the gym for at least 15 days"
#     elif month == 'march':
#         challenge_text = "Save money till ksh 15000"
#     elif month == 'april':
#         challenge_text = "Adopt a new productive hobby"
#     else: 
#         return HttpResponseNotFound("That Month is Not Supported") 
#     return HttpResponse(challenge_text)
    try:
        challenge_text = monthly_challenges[month] 
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("That Month is Not Supported")
    
