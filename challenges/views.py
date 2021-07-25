from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat for the enire month !",
    "february": "Walk for at least 20 minutes every day!",
    "march" : "learn django more than 20 mins every day",
    "april" : "learn django more than 20 mins every day",
    "may" : "learn django more than 20 mins every day",
    "june" : "learn django more than 20 mins every day",
    "july" : "learn django more than 20 mins every day",
    "august" : "learn django more than 20 mins every day",
    "september" : "learn django more than 20 mins every day",
    "october" : "learn django more than 20 mins every day",
    "november" : "learn django more than 20 mins every day",
    "december" : "learn django more than 20 mins every day"
}
# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months : 
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"


    respose_data = """
        <ul>
            <li><a href="/challenges/january">January</li>
            <li><a href="/challenges/february">February</li>
            <li><a href="/challenges/march">March</li>
            <li><a href="/challenges/april">April</li>
            <li><a href="/challenges/may">May</li>
            <li><a href="/challenges/june">June</li>
            <li><a href="/challenges/july">July</li>
            <li><a href="/challenges/august">August</li>
            <li><a href="/challenges/september">September</li>
            <li><a href="/challenges/october">October</li>
            <li><a href="/challenges/november">November</li>
            <li><a href="/challenges/december">December</li>
        </ul>
    """
    return HttpResponse()


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args= [redirect_month])  #challenge/january  #reverse makes possible to convert "month-challenge" to "challenege", it is args because of dictionary we get args 
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try :
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except :
        return HttpResponseNotFound("This month is not supported !")
    