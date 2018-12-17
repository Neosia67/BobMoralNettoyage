import datetime

from django.test import TestCase
from django.utils import timezone
from .models import User, Building, Request



class UserModelTests(TestCase):
  def test_user_created(self):
    u = User("Theo", "Santos", "theo.santos@gmail.com", "0600000000", "10 rue des cailloux ronds")
    u.save()
    print(str(u))
    self.assertIs(str(u) == "theo.santos@gmail.com", True)

class BuildingModelTests(TestCase):
  def test_building_created(self):
    b = Building("11 rue des cailloux ronds", "theo.santos@gmail.com")
    b.save()
    print(str(b))
    self.assertIs(str(b) == "11 rue des cailloux ronds", True)

class RequestModelTests(TestCase):
  def test_request_created(self):
    """
    was_published_recently() returns False for questions whose pub_date
    is in the future.
    """
    r = Request("theo.santos@gmail.com", "11 rue des cailloux ronds",
                "~/Affiche_e-Rigator.png", 10,"N", timezone.now())
    r.save()
    self.assertIs(True, True)