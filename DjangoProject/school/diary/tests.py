# from django.test import TestCase
import unittest

from django.test import Client
from django.urls import reverse
import pytest
from pytest_django.asserts import assertQuerysetEqual

from .models import WeekDay


# Create your tests here.
@pytest.mark.urls("diary.urls")
def test_index_redirects(client):
    response = client.get("/")
    assert response.status_code == 302


@pytest.mark.urls("diary.urls")
def test_index_redirects_to_my_week(client):
    response = client.get("/")
    assert response.status_code == 302
    assert response.url == reverse("my_week")


@pytest.mark.django_db
class DataBaseTests(unittest.TestCase):
    def setUp(self):
        for day in ["Mon", "Tue", "Wed"]:
            WeekDay.objects.create(day=day)
        self.client = Client()

    def test_my_week_has_three_days(self):
        response_clean_database = self.client.get(reverse("my_week"))
        weeks_days = WeekDay.objects.all()
        assertQuerysetEqual(response_clean_database.context["objects"], weeks_days)
        # for day in ["Mon", "Tue", "Wed"]:
        #     WeekDay.objects.create(day=day)
        weeks_days_updated = WeekDay.objects.all()
        response_fulfilled_database = self.client.get("/week/")
        assertQuerysetEqual(
            response_fulfilled_database.context["objects"], weeks_days_updated, ordered=False
        )
        assert len(response_fulfilled_database.context["days"]) == 3
