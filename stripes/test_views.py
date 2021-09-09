from django.test import TestCase
from django.urls import reverse

from . import views


class StripesRootViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.view = views.stripes_root
        cls.test_url = reverse('stripes:stripes_root')

    def setUp(self):
        self.response = self.client.get(self.test_url)

    def test_request_get_method(self):
        self.assertEqual(self.response.status_code, 200)
