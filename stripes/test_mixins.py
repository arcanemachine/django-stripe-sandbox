from django.contrib import messages
from django.test import RequestFactory, TestCase
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, TemplateView,\
    UpdateView
from unittest import mock

from .views import CustomerDeleteView
from .models import Customer
from .mixins import CommonViewMixin, CustomerViewMixin,\
    StripeSuccessMessageMixin
from django_stripe_sandbox import factories as f


class DummyDeleteView(StripeSuccessMessageMixin, DeleteView):
    model = Customer


# mixins
class StripeSuccessMessageMixinTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.mixin = StripeSuccessMessageMixin

    def test_attribute_value_success_message(self):
        self.assertEqual(self.mixin.success_message, 'success')

    @mock.patch(
        'django.contrib.messages.success', mock.Mock(return_value=True))
    def test_method_delete_calls_function_messages_success(self):
        test_customer = f.CustomerFactory()

        test_view = DummyDeleteView()
        request = RequestFactory().get('/')
        test_view.setup(request)

        # add mocks for test view
        test_view.get_success_url = mock.Mock(return_value='/')
        test_view.get_object =\
            mock.Mock(return_value=test_customer)

        # call delete() and check that the success message has been added
        test_view.delete(request)
        messages.success.assert_called()


# create a dummy mixin to avoid duplicate boilerplate in dummy views
class DummyMixin:
    object = None
    fields = '__all__'

    def get_queryset(self):
        return Customer.objects.none()


class DummyMixinTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.mixin = DummyMixin

    def test_attribute_object_value(self):
        self.assertIsNone(self.mixin.object)

    def test_attribute_fields_value(self):
        self.assertEqual(self.mixin.fields, '__all__')

    def test_method_get_queryset_returns_empty_queryset(self):
        self.assertEqual(set(self.mixin().get_queryset()),
                         set(Customer.objects.none()))


class CommonViewMixinTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.mixin = CommonViewMixin
        cls.request = RequestFactory().get('/')

    def test_attribute_context_object_name_value(self):
        self.assertEqual(self.mixin.context_object_name, 'object')

    def test_context_has_action_verb_none_in_templateview(self):
        class DummyTemplateView(self.mixin, TemplateView):
            pass

        self.dummy_templateview = DummyTemplateView()
        self.dummy_templateview.setup(self.request)

        context = self.dummy_templateview.get_context_data()
        self.assertEqual(context['action_verb'], None)

    def test_context_has_action_verb_create_in_createview(self):
        class DummyCreateView(self.mixin, DummyMixin, CreateView):
            pass

        self.dummy_createview = DummyCreateView()
        self.dummy_createview.setup(self.request)

        context = self.dummy_createview.get_context_data()
        self.assertEqual(context['action_verb'], 'create')

    def test_context_has_action_verb_create_in_updateview(self):
        class DummyUpdateView(self.mixin, DummyMixin, UpdateView):
            pass

        self.dummy_updateview = DummyUpdateView()
        self.dummy_updateview.setup(self.request)

        context = self.dummy_updateview.get_context_data()
        self.assertEqual(context['action_verb'], 'update')


class CustomerViewMixinTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.mixin = CustomerViewMixin

    def test_attribute_model_value(self):
        self.assertEqual(self.mixin.model.__name__, 'Customer')

    def test_attribute_pk_url_kwarg_value(self):
        self.assertEqual(self.mixin.pk_url_kwarg, 'customer_pk')

    def test_attribute_success_url_value(self):
        self.assertEqual(
            self.mixin.success_url, reverse_lazy('stripes:customer_list'))
