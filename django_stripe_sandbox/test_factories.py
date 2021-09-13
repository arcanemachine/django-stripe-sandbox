from django.test import TestCase

from . import factories as f


class CustomerFactoryTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_object = f.CustomerFactory()

    def test_object_uses_expected_model(self):
        self.assertEqual(self.test_object.__class__.__name__, 'Customer')


class PaymentMethodFactoryTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_object = f.PaymentMethodFactory()

    def test_object_uses_expected_model(self):
        self.assertEqual(self.test_object.__class__.__name__, 'PaymentMethod')
