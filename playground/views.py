from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

monthly_tasks = {
    "january": "Do 10 hours of code",
    "february": "Do 20 hours of code",
    "march": "Do 30 hours of code",
    "april": "Do 40 hours of code",
    "may": "Do 50 hours of code",
    "june": "Do 60 hours of code",
    "july": "Do 70 hours of code",
    "august": "Do 80 hours of code",
    "september": "Do 90 hours of code",
    "october": "Do 100 hours of code",
    "november": "Do 110 hours of code",
    "december": None
}


def index(request):
    list_items = ""
    months = list(monthly_tasks.keys())
    return render(request, "playground/index.html", {
        "months":months
    })


def monthly_task_by_number(request, month):
    months = list(monthly_tasks.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month-1]
    redirected_path = reverse("month-task", args=[redirect_month])
    return HttpResponseRedirect(redirected_path)


def monthly_task(request, month):
    try:
        monthly_text = monthly_tasks[month]
        return render(request, "playground/playground.html", {
            "text": monthly_text,
            "month": month.capitalize()
        })
    except:
        raise Http404()
