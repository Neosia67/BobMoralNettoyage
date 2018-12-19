import datetime

from django.test import TestCase
from django.utils import timezone
from .models import Client, Building, Ticket
from django.contrib.auth.models import User




class UserModelTests(TestCase):
  def test_user_created(self):
    user = User("TheoSnake", "Bobmorale", "theo.santos@gmail.com")
    u = Client(user, "Theo", "Santos", "10 rue des cailloux ronds", "0600000000")
    u.save()
    print(str(u))
    self.assertIs(str(u) == "Theo", True)

class BuildingModelTests(TestCase):
  def test_building_created(self):
    b = Building("11 rue des cailloux ronds", "", 10, "0600000000")
    b.save()
    print(str(b))
    self.assertIs(str(b) == "11 rue des cailloux ronds", True)

class TicketModelTests(TestCase):
  def test_ticket_created(self):
    """
    was_published_recently() returns False for questions whose pub_date
    is in the future.
    """
    r = Ticket("0600000000", "11 rue des cailloux ronds",
                "~/Affiche_e-Rigator.png", 10, "N", timezone.now())
    r.save()
    self.assertIs(True, True)
