from django.test import TestCase

from .models import AbstractModel
from django_stripe_sandbox import factories as f


class AbstractModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_model = AbstractModel.objects.create()

    def test_method_get_absolute_url(self):
        self.assertEqual(self.test_model.get_absolute_url(), '/')

    def test_method_str(self):
        self.assertEqual(self.test_model.__str__(), str(self.test_model.id))


class CustomerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_model = f.CustomerFactory()

    def test_model_object_name(self):
        # covered by test_factories.py
        pass

    def test_model_base_class(self):
        self.assertEqual(
            self.test_model.__class__.__bases__[0].__name__, 'AbstractModel')

    def test_field_stripe_customer_field_type(self):
        self.assertEqual(self.test_model._meta.get_field(
            'stripe_customer').get_internal_type(), 'JSONField')

    def test_field_stripe_customer_is_blank(self):
        self.assertEqual(
            self.test_model._meta.get_field('stripe_customer').blank, True)

    def test_field_stripe_customer_is_null(self):
        self.assertEqual(
            self.test_model._meta.get_field('stripe_customer').null, True)
