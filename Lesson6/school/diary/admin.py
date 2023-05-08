from django.contrib import admin

# Register your models here.
from .models import WeekDay


class WeekDayAdmin(admin.ModelAdmin):
    list_display = ('title', 'note')


admin.site.register(WeekDay, WeekDayAdmin)


