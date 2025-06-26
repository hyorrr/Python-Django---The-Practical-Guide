from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string # to bring some templates(html files)

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
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index_inheritance.html", {
        "months": months
    })


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

    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        #response_data = render_to_string("challenges/challenge.html") # read the template and render by string
        # return HTML
        #return HttpResponse(response_data)  
        return render(request, "challenges/challenge_inheritance.html", {
            "month_name": month,
            "text_challenge": challenge_text # context 라 불림 # for dynamic content
        })
    except:
        # return HttpResponseNotFound("<h1>This month is not supported!</h1>")
        # respone_data = render_to_string("404.html")
        # return HttpResponseNotFound(respone_data) # 개발자모드에서 network 확인시 404 로 뜸
        raise Http404() # 자동적으로 /template/404.html 파일을 불러옴, 파일 이름은 꼭 404.html 여야함