from django.http import HttpResponse
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

    my_week = WeekDay.objects.all()
    return HttpResponse(my_week)


