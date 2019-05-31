from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from siteApp.models import Login

class LoginTestCase(TestCase):
    def setUp(self):
        Login.objects.create(name="jose", sound="123")
        Login.objects.create(name="jose2", sound="1234")