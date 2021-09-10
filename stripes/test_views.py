from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from . import views


# stripes_root
class StripesRootViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.view = views.stripes_root
        cls.test_url = reverse('stripes:stripes_root')

    def setUp(self):
        self.response = self.client.get(self.test_url)

    def test_method_get(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'stripes/stripes_root.html')


# customer
class CustomerListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.view = views.CustomerListView
        cls.test_url = reverse('stripes:customer_list')

    def test_mixins(self):
        expected_mixins =\
            ['ContextObjectInfoMixin', 'CommonViewMixin', 'CustomerViewMixin',
             'StripeSuccessMessageMixin', 'ListView']
        actual_mixins = [mixin.__name__ for mixin in self.view.__bases__]
        for expected_mixin in expected_mixins:
            self.assertIn(expected_mixin, actual_mixins)


class CustomerCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.view = views.CustomerCreateView
        cls.test_url = reverse('stripes:customer_create')

    def test_mixins(self):
        expected_mixins =\
            ['ContextObjectInfoMixin', 'CommonViewMixin', 'CustomerViewMixin',
             'StripeSuccessMessageMixin', 'CreateView']
        actual_mixins = [mixin.__name__ for mixin in self.view.__bases__]
        for expected_mixin in expected_mixins:
            self.assertIn(expected_mixin, actual_mixins)
