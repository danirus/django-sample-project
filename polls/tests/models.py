import datetime
from polls.models import Poll, Choice
from django.test import TestCase as DjangoTestCase
from django.utils.timezone import now


class SimplePollTestCase(DjangoTestCase):
    def test_create(self):
        poll = Poll.objects.create(question="What's up", pub_date=now())
        self.assertEqual(Poll.objects.count(), 1)


class SimpleChoiceTestCase(DjangoTestCase):
    def setUp(self):
        self.poll = Poll.objects.create(
            question="What's up", pub_date=now())

    def test_create(self):
        choice = Choice.objects.create(poll=self.poll, choice_text="Nothing")
        self.assertEqual(Choice.objects.count(), 1)
