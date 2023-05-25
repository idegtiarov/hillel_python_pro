from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.urls import reverse
from django.views.generic import DetailView, FormView, ListView

from .forms import NoteForm
from .models import Note, WeekDay


def index(request):
    return redirect("my_week")


class DaysList(ListView):
    model = WeekDay
    template_name = "diary/week.html"
    context_object_name = "days"


def my_week(request):
    # week_day = WeekDay(title="Fri", note="Some interesting thing should happens")
    # response = f"on a week_day: {week_day.title}, there is going to: {week_day.note}"
    template = loader.get_template("diary/week.html")
    context = {"days": WeekDay.objects.all()}

    return HttpResponse(template.render(context, request))


class DayDetail(DetailView):
    model = WeekDay
    # template_name = "diary/weekday_detail.html"


def my_day(request, week_day_id):
    day = get_object_or_404(WeekDay, pk=week_day_id)
    return render(request, "diary/weekday_detail.html", {"week_day": day})


class NoteFormView(FormView):
    form_class = NoteForm
    template_name = "diary/weekday_detail.html"

    def get_form_kwargs(self):
        form_kwarg = super().get_form_kwargs()
        form_kwarg["key_id"] = self.kwargs["pk"]
        return form_kwarg

    def form_valid(self, form):
        week_day = get_object_or_404(WeekDay, pk=self.kwargs["pk"])
        Note.objects.create(
            week_day=week_day,
            title=form.cleaned_data["title"],
            msg=form.cleaned_data["msg"],
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["object"] = get_object_or_404(WeekDay, pk=self.kwargs["pk"])
        return context

    def get_success_url(self):
        return reverse("week_day", kwargs={"pk": self.kwargs["pk"]})


def add_note(request, week_day_id):
    week_day = get_object_or_404(WeekDay, pk=week_day_id)
    form_data = NoteForm(request.POST)
    if form_data.is_valid():
        Note.objects.create(
            week_day=week_day,
            title=form_data.cleaned_data["title"],
            msg=form_data.cleaned_data["msg"],
        )
    return render(
        request,
        "diary/weekday_detail.html",
        {"week_day": week_day, "error_message": form_data.errors},
    )
