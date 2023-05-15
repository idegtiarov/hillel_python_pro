from django.contrib import admin

# Register your models here.
from .models import WeekDay, Note


class WeekDayAdmin(admin.ModelAdmin):
    list_display = ("day",)


class NoteAdmin(admin.ModelAdmin):
    list_display = ("title", "msg",)


admin.site.register(WeekDay, WeekDayAdmin)
admin.site.register(Note, NoteAdmin)
