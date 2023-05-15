from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader

from .forms import NoteForm
from .models import Note, WeekDay


def index(request):
    return redirect('my_week')



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


def add_note(request, week_day_id):
    week_day = get_object_or_404(WeekDay, pk=week_day_id)
    form_data = NoteForm(request.POST)
    if form_data.is_valid():
        Note.objects.create(week_day=week_day, title=form_data.cleaned_data['title'], msg=form_data.cleaned_data['msg'])
    return render(request, "diary/week_day.html", {"week_day": week_day, "error_message": form_data.errors})