from django.urls import resolve, reverse
from django.test import SimpleTestCase


class CustomerListViewUrlTest(SimpleTestCase):
    def test_url_reverse(self):
        self.assertEqual(reverse('stripes:customer_list'), '/customer/')

    def test_url_resolve(self):
        self.assertEqual(
            resolve('/customer/').view_name, 'stripes:customer_list')


class CustomerCreateViewUrlTest(SimpleTestCase):
    def test_url_reverse(self):
        self.assertEqual(
            reverse('stripes:customer_create'), '/customer/create/')

    def test_url_resolve(self):
        self.assertEqual(
            resolve('/customer/create/').view_name, 'stripes:customer_create')


class CustomerDetailViewUrlTest(SimpleTestCase):
    def test_url_reverse(self):
        self.assertEqual(
            reverse('stripes:customer_detail', kwargs={'customer_pk': 1}),
            '/customer/1/')

    def test_url_resolve(self):
        self.assertEqual(
            resolve('/customer/1/').view_name, 'stripes:customer_detail')


class CustomerUpdateViewUrlTest(SimpleTestCase):
    def test_url_reverse(self):
        self.assertEqual(
            reverse('stripes:customer_update', kwargs={'customer_pk': 1}),
            '/customer/1/update/')

    def test_url_resolve(self):
        self.assertEqual(
            resolve('/customer/1/update/').view_name,
            'stripes:customer_update')


class CustomerDeleteViewUrlTest(SimpleTestCase):
    def test_url_reverse(self):
        self.assertEqual(
            reverse('stripes:customer_delete', kwargs={'customer_pk': 1}),
            '/customer/1/delete/')

    def test_url_resolve(self):
        self.assertEqual(
            resolve('/customer/1/delete/').view_name,
            'stripes:customer_delete')


class CustomerNewestDeleteViewUrlTest(SimpleTestCase):
    def test_url_reverse(self):
        self.assertEqual(
            reverse('stripes:customer_delete_newest'),
            '/customer/newest/delete/')

    def test_url_resolve(self):
        self.assertEqual(
            resolve('/customer/newest/delete/').view_name,
            'stripes:customer_delete_newest')
