from polls.utils import do_otherthing
from django.test import TestCase as DjangoTestCase

class DoOtherthingTestCase(DjangoTestCase):
    def test_do_otherthing(self):
        self.assertEqual(do_otherthing(), 11)

