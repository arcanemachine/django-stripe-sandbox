from django.test import TestCase

from .models import AbstractModel, Customer, PaymentMethod
from django_stripe_sandbox import factories as f


class AbstractModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_model = AbstractModel.objects.create()

    def test_method_get_absolute_url(self):
        absolute_url = self.test_model.get_absolute_url()
        self.assertEqual(absolute_url, '/')

    def test_method_str(self):
        string_representation = self.test_model.__str__()
        self.assertEqual(string_representation, str(self.test_model.id))


class CustomerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_customer = f.CustomerFactory()

    def test_model_object_name(self):
        # covered by test_factories.py
        pass

    def test_model_base_class_name(self):
        base_class_name = self.test_customer.__class__.__bases__[0].__name__
        self.assertEqual(base_class_name, 'AbstractModel')

    def test_field_stripe_customer_field_type(self):
        field_type =\
            self.test_customer._meta.get_field(
                'stripe_customer').get_internal_type()
        self.assertEqual(field_type, 'JSONField')

    def test_field_stripe_customer_is_blank(self):
        is_blank = self.test_customer._meta.get_field('stripe_customer').blank
        self.assertEqual(is_blank, True)

    def test_field_stripe_customer_is_null(self):
        is_null = self.test_customer._meta.get_field('stripe_customer').null
        self.assertEqual(is_null, True)

    def test_method_save_creates_stripe_customer(self):
        current_test_customer = Customer()

        # stripe_customer is None before save()
        self.assertIsNone(current_test_customer.stripe_customer)

        # stripe_customer exists after save() and contains expected data
        current_test_customer.save()
        self.assertIsNotNone(current_test_customer.stripe_customer)
        self.assertIn('id', current_test_customer.stripe_customer.keys())


class PaymentMethodModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_paymentmethod = f.PaymentMethodFactory()

    def test_model_object_name(self):
        # covered by test_factories.py
        pass

    def test_model_base_class_name(self):
        base_class_name =\
            self.test_paymentmethod.__class__.__bases__[0].__name__
        self.assertEqual(base_class_name, 'Model')

    def test_field_stripe_paymentmethod_field_type(self):
        field_type =\
            self.test_paymentmethod._meta.get_field('stripe_paymentmethod')\
                .get_internal_type()
        self.assertEqual(field_type, 'JSONField')

    def test_field_stripe_paymentmethod_is_blank(self):
        is_blank =\
            self.test_paymentmethod._meta.get_field('stripe_paymentmethod')\
                .blank
        self.assertEqual(is_blank, True)

    def test_field_stripe_paymentmethod_is_null(self):
        is_null = self.test_paymentmethod._meta\
            .get_field('stripe_paymentmethod').null
        self.assertEqual(is_null, True)

    def test_method_save_creates_stripe_paymentmethod(self):
        current_test_paymentmethod = PaymentMethod()

        # stripe_customer is None before save()
        self.assertIsNone(current_test_paymentmethod.stripe_paymentmethod)

        # stripe_customer exists after save() and contains expected data
        current_test_paymentmethod.save()
        self.assertIsNotNone(current_test_paymentmethod.stripe_paymentmethod)
        self.assertIn(
            'id', current_test_paymentmethod.stripe_paymentmethod.keys())
