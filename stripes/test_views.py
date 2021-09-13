import json
from django.test import TestCase
from django.urls import reverse

from .models import Customer, PaymentMethod
from . import views
from django_stripe_sandbox import factories as f

common_mixins =\
    ['ContextObjectInfoMixin', 'CommonViewMixin', 'StripeSuccessMessageMixin']


# stripes_root
class StripesRootViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.view = views.stripes_root
        cls.test_url = reverse('stripes:stripes_root')

    def test_method_get(self):
        response = self.client.get(self.test_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stripes/stripes_root.html')


# customer
customer_mixins = common_mixins + ['CustomerViewMixin']


class CustomerListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.view = views.CustomerListView
        cls.test_url = reverse('stripes:customer_list')

    def test_mixins(self):
        expected_mixins = customer_mixins + ['ListView']
        actual_mixins = [mixin.__name__ for mixin in self.view.__bases__]
        for expected_mixin in expected_mixins:
            self.assertIn(expected_mixin, actual_mixins)

    def test_method_get(self):
        response = self.client.get(self.test_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stripes/customer_list.html')


class CustomerDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_customer = f.CustomerFactory()
        cls.view = views.CustomerDetailView
        cls.test_url = reverse('stripes:customer_detail', kwargs={
            'customer_pk': test_customer.pk})

    def test_mixins(self):
        expected_mixins = customer_mixins + ['DetailView']
        actual_mixins = [mixin.__name__ for mixin in self.view.__bases__]
        for expected_mixin in expected_mixins:
            self.assertIn(expected_mixin, actual_mixins)

    def test_method_get(self):
        response = self.client.get(self.test_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stripes/customer_detail.html')


class CustomerCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.view = views.CustomerCreateView
        cls.test_url = reverse('stripes:customer_create')

    def test_mixins(self):
        expected_mixins = customer_mixins + ['CreateView']
        actual_mixins = [mixin.__name__ for mixin in self.view.__bases__]
        for expected_mixin in expected_mixins:
            self.assertIn(expected_mixin, actual_mixins)

    # request.GET
    def test_method_get(self):
        response = self.client.get(self.test_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stripes/customer_form.html')

    # request.POST
    def test_method_post_creates_new_customer(self):
        # get object count before making POST request
        object_count_old = Customer.objects.count()

        # create POST request
        response = self.client.post(self.test_url, follow=True)
        self.assertEqual(response.status_code, 200)

        # object count incremented by one
        object_count_new = Customer.objects.count()
        self.assertEqual(object_count_old + 1, object_count_new)


class CustomerUpdateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_customer = f.CustomerFactory()
        cls.view = views.CustomerUpdateView
        cls.test_url = reverse('stripes:customer_update', kwargs={
            'customer_pk': cls.test_customer.pk})

    def test_mixins(self):
        expected_mixins = customer_mixins + ['UpdateView']
        actual_mixins = [mixin.__name__ for mixin in self.view.__bases__]
        for expected_mixin in expected_mixins:
            self.assertIn(expected_mixin, actual_mixins)

    def test_method_get(self):
        response = self.client.get(self.test_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stripes/customer_form.html')

    # request.POST
    def test_method_post_updates_object(self):
        # create POST request
        form_data = {'stripe_customer': '{"key": "value"}'}  # proper JSON
        response = self.client.post(self.test_url, data=form_data, follow=True)
        self.assertEqual(response.status_code, 200)

        # object contains updated data
        self.test_customer.refresh_from_db()
        self.assertEqual(
            self.test_customer.stripe_customer,
            json.loads(form_data['stripe_customer']))


class CustomerDeleteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.obj = Customer
        test_customer = f.CustomerFactory()
        cls.view = views.CustomerDeleteView
        cls.test_url = reverse('stripes:customer_delete', kwargs={
            'customer_pk': test_customer.pk})

    def test_mixins(self):
        expected_mixins = customer_mixins + ['DeleteView']
        actual_mixins = [mixin.__name__ for mixin in self.view.__bases__]
        for expected_mixin in expected_mixins:
            self.assertIn(expected_mixin, actual_mixins)

    def test_method_get(self):
        response = self.client.get(self.test_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'stripes/customer_confirm_delete.html')

    # request.POST
    def test_method_post_deletes_object(self):
        # get object count before making POST request
        object_count_old = Customer.objects.count()

        # create POST request
        response = self.client.post(self.test_url, follow=True)

        # should redirect to customer's absolute url
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stripes/customer_list.html')

        # object count incremented by one
        object_count_new = Customer.objects.count()
        self.assertEqual(object_count_old - 1, object_count_new)


class CustomerNewestDeleteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.obj = Customer
        cls.test_customer = f.CustomerFactory()
        cls.view = views.CustomerDeleteView
        cls.test_url = reverse('stripes:customer_delete_newest')

    def test_mixins(self):
        expected_mixins = customer_mixins + ['DeleteView']
        actual_mixins = [mixin.__name__ for mixin in self.view.__bases__]
        for expected_mixin in expected_mixins:
            self.assertIn(expected_mixin, actual_mixins)

    # get_object()
    def test_method_get_object_returns_last_customer(self):
        # try with self.test_customer
        response = self.client.get(self.test_url)
        view_instance = response.context['view']
        self.assertEqual(view_instance.get_object().pk, self.test_customer.pk)

        # try with new Customer
        test_customer = f.CustomerFactory()
        response = self.client.get(self.test_url)
        view_instance = response.context['view']
        self.assertEqual(view_instance.get_object().pk, test_customer.pk)

    # request.GET
    def test_method_get(self):
        response = self.client.get(self.test_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'stripes/customer_confirm_delete.html')

    # request.POST
    def test_method_post_deletes_object(self):
        # get object count before making POST request
        object_count_old = Customer.objects.count()

        # create POST request
        response = self.client.post(self.test_url, follow=True)

        # should redirect to customer's absolute url
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stripes/customer_list.html')

        # object count incremented by one
        object_count_new = Customer.objects.count()
        self.assertEqual(object_count_old - 1, object_count_new)


# paymentmethod
paymentmethod_mixins = common_mixins + ['PaymentMethodViewMixin']


class PaymentMethodListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.view = views.PaymentMethodListView
        cls.test_url = reverse('stripes:paymentmethod_list')

    def test_mixins(self):
        expected_mixins = paymentmethod_mixins + ['ListView']
        actual_mixins = [mixin.__name__ for mixin in self.view.__bases__]
        for expected_mixin in expected_mixins:
            self.assertIn(expected_mixin, actual_mixins)

    def test_method_get(self):
        response = self.client.get(self.test_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stripes/paymentmethod_list.html')


class PaymentMethodDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_paymentmethod = f.PaymentMethodFactory()
        cls.view = views.PaymentMethodDetailView
        cls.test_url = reverse('stripes:paymentmethod_detail', kwargs={
            'paymentmethod_pk': test_paymentmethod.pk})

    def test_mixins(self):
        expected_mixins = paymentmethod_mixins + ['DetailView']
        actual_mixins = [mixin.__name__ for mixin in self.view.__bases__]
        for expected_mixin in expected_mixins:
            self.assertIn(expected_mixin, actual_mixins)

    def test_method_get(self):
        response = self.client.get(self.test_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stripes/paymentmethod_detail.html')


class PaymentMethodCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.view = views.PaymentMethodCreateView
        cls.test_url = reverse('stripes:paymentmethod_create')

    def test_mixins(self):
        expected_mixins = paymentmethod_mixins + ['CreateView']
        actual_mixins = [mixin.__name__ for mixin in self.view.__bases__]
        for expected_mixin in expected_mixins:
            self.assertIn(expected_mixin, actual_mixins)

    # request.GET
    def test_method_get(self):
        response = self.client.get(self.test_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stripes/paymentmethod_form.html')

    # request.POST
    def test_method_post_creates_new_paymentmethod(self):
        # get object count before making POST request
        object_count_old = PaymentMethod.objects.count()

        # create POST request
        response = self.client.post(self.test_url, follow=True)
        self.assertEqual(response.status_code, 200)

        # object count incremented by one
        object_count_new = PaymentMethod.objects.count()
        self.assertEqual(object_count_old + 1, object_count_new)


class PaymentMethodUpdateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_paymentmethod = f.PaymentMethodFactory()
        cls.view = views.PaymentMethodUpdateView
        cls.test_url = reverse('stripes:paymentmethod_update', kwargs={
            'paymentmethod_pk': cls.test_paymentmethod.pk})

    def test_mixins(self):
        expected_mixins = paymentmethod_mixins + ['UpdateView']
        actual_mixins = [mixin.__name__ for mixin in self.view.__bases__]
        for expected_mixin in expected_mixins:
            self.assertIn(expected_mixin, actual_mixins)

    def test_method_get(self):
        response = self.client.get(self.test_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stripes/paymentmethod_form.html')

    # request.POST
    def test_method_post_updates_object(self):
        # create POST request
        form_data = {'stripe_paymentmethod': '{"key": "value"}'}  # proper JSON
        response = self.client.post(self.test_url, data=form_data, follow=True)
        self.assertEqual(response.status_code, 200)

        # object contains updated data
        self.test_paymentmethod.refresh_from_db()
        self.assertEqual(
            self.test_paymentmethod.stripe_paymentmethod,
            json.loads(form_data['stripe_paymentmethod']))


class PaymentMethodDeleteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.obj = PaymentMethod
        test_paymentmethod = f.PaymentMethodFactory()
        cls.view = views.PaymentMethodDeleteView
        cls.test_url = reverse('stripes:paymentmethod_delete', kwargs={
            'paymentmethod_pk': test_paymentmethod.pk})

    def test_mixins(self):
        expected_mixins = paymentmethod_mixins + ['DeleteView']
        actual_mixins = [mixin.__name__ for mixin in self.view.__bases__]
        for expected_mixin in expected_mixins:
            self.assertIn(expected_mixin, actual_mixins)

    def test_method_get(self):
        response = self.client.get(self.test_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'stripes/paymentmethod_confirm_delete.html')

    # request.POST
    def test_method_post_deletes_object(self):
        # get object count before making POST request
        object_count_old = PaymentMethod.objects.count()

        # create POST request
        response = self.client.post(self.test_url, follow=True)

        # should redirect to paymentmethod's absolute url
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'stripes/paymentmethod_list.html')

        # object count incremented by one
        object_count_new = PaymentMethod.objects.count()
        self.assertEqual(object_count_old - 1, object_count_new)
