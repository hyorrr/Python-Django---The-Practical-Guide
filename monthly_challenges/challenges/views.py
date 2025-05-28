from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat of the entire month!",
    "feburary": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat of the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat of the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat of the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Learn Django for at least 20 minutes every day!"
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize() # only first letter is upper and rests are lower
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # "<li><a href="...">January</a></li><li><a href="...">Feburary</a></li>..."

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

# def january(request):
#     return HttpResponse("Eat no meat of the entire month!")

# def feburary(request):
#     return HttpResponse("Walk for at least 20 minutes every day!")

# def march(request):
#     return HttpResponse("Learn Django for at least 20 minutes every day!")
    

def monthly_challenge_by_number(request, month):
    # for change number to string
    months = list(monthly_challenges.keys())

    # check the error in case the month number is over 12
    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month</h1>")
    
    redirect_month = months[month - 1]
    # month 에 args 값을 넣어줌
    # month-challenge라는 URL 이름에 redirect_month 값을 넣어서 완성된 URL 경로 문자열을 만드는 것!
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
    # if url is changed the code would be not easy to maintain
    # return HttpResponseRedirect("/challenges/" + redirect_month)
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        # return HTML
        return HttpResponse(response_data)
    # for dynamic segements
    # if month == "january":
    #     challenge_text = "Eat no meat of the entire month!"
    # elif month == "feburary":
    #     challenge_text = "Walk for at least 20 minutes every day!"
    # elif month == "march":
    #     challenge_text = "Learn Django for at least 20 minutes every day!"
    # else:
    #     return HttpResponseNotFound("This month is not supported!")   
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
