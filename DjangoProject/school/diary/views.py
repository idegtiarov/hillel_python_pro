from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import WeekDay

index_template = f"""
    <form action="/login/" method="POST">
      <div>
         <label for="new_item">Please enter your name!</label>
         <input name="name" id="name" value="your name" />
      </div>
      <div>
         <label for="new_item">Please enter the language!</label>
         <input name="language" id="lang" value="Python" />
      </div>
        <button>Send my choice</button>
    </form>
"""


def index(request):
    return HttpResponse(index_template)


def login(request):
    if request.POST:
        name = request.POST.get("name")
        language = request.POST.get("language")
        response = f"Username: {name}, language: {language}"
    else:
        response = "Please login on the home page"

    return HttpResponse(response)


def my_week(request):
    # week_day = WeekDay(title="Fri", note="Some interesting thing should happens")
    # response = f"on a week_day: {week_day.title}, there is going to: {week_day.note}"
    template = loader.get_template("diary/week.html")
    context = {
        "days": WeekDay.objects.all()
    }

    return HttpResponse(template.render(context, request))


def my_day(request, week_day_id):
    day = get_object_or_404(WeekDay, pk=week_day_id)
    return render(request, "diary/week_day.html", {"week_day": day})

