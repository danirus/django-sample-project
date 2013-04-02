import datetime
from polls.models import Poll, Choice
from django.test import TestCase as DjangoTestCase


class SimplePollTestCase(DjangoTestCase):
    def test_create(self):
        poll = Poll.objects.create(question="What's up",
                                   pub_date=datetime.datetime(2013, 1, 1))
        self.assert_(Poll.objects.count() == 1)


class SimpleChoiceTestCase(DjangoTestCase):
    def setUp(self):
        self.poll = Poll.objects.create(
            question="What's up",
            pub_date=datetime.datetime(2013, 1, 1))

    def test_create(self):
        choice = Choice.objects.create(poll=self.poll, choice_text="Nothing")
        self.assert_(Choice.objects.count() == 1)
