from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as AuthLoginView
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.urls import reverse
from django.views.generic import CreateView, DetailView, FormView, ListView

from .forms import NoteForm
from .models import Note, WeekDay
from .mixins import MixinUserFilter


def index(request):
    session = request.session
    print(f"{session.get('key')}")
    session[123] = {'all': 'empty'}

    return redirect("my_week")


class RegisterCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'diary/login.html'
    success_url = '/'

# NOTE: in class we missed to use LoginView from django.contrib.auth.views and uses instead generic FormView
#  If we use generic view additional step is required to be called: https://github.com/django/django/blob/main/django/contrib/auth/__init__.py#L94
class LoginView(AuthLoginView):
    template_name = "diary/login.html"


def logout(request):
    auth_logout(request)
    return redirect('index')


class DaysList(ListView):
    model = WeekDay
    template_name = "diary/week.html"
    context_object_name = "days"

    def get_queryset(self):
        data = super().get_queryset().filter(user=self.request.user)
        return data

def my_week(request):
    print(f"{request.user.is_authenticated}")
    if not request.user.is_authenticated:
        return redirect('login')
    # week_day = WeekDay(title="Fri", note="Some interesting thing should happens")
    # response = f"on a week_day: {week_day.title}, there is going to: {week_day.note}"
    template = loader.get_template("diary/week.html")
    context = {"days": WeekDay.objects.all()}

    return HttpResponse(template.render(context, request))


class DayDetail(MixinUserFilter, DetailView):
    model = WeekDay
    # template_name = "diary/weekday_detail.html"


def my_day(request, pk):
    print(f"{request.session.get('123')}")
    request.session["key"] = 123671327819
    day = get_object_or_404(WeekDay, pk=pk)
    return render(request, "diary/weekday_detail.html", {"object": day})


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
