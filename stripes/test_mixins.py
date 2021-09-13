from django.contrib import messages
from django.test import RequestFactory, TestCase
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, TemplateView,\
    UpdateView
from unittest.mock import Mock, patch

from .models import AbstractModel, Customer, PaymentMethod
from . import mixins
from django_stripe_sandbox import factories as f

generic_request = RequestFactory().get('/')


# StripeSuccessMessageMixin
class DummySSMCreateView(mixins.StripeSuccessMessageMixin, CreateView):
    model = AbstractModel


class DummySSMUpdateView(mixins.StripeSuccessMessageMixin, UpdateView):
    model = AbstractModel


class DummySSMDeleteView(mixins.StripeSuccessMessageMixin, DeleteView):
    model = AbstractModel


class StripeSuccessMessageMixinTest(TestCase):
    cleaned_data_empty = {}

    @classmethod
    def setUpTestData(cls):
        cls.mixin = mixins.StripeSuccessMessageMixin

    def test_attribute_value_success_message(self):
        self.assertEqual(self.mixin.success_message, 'success')

    # delete()
    @patch('django.contrib.messages.success', Mock(return_value=True))
    def test_method_delete_calls_function_messages_success(self):
        test_customer = f.CustomerFactory()

        test_view = DummySSMDeleteView()
        test_view.setup(generic_request)

        # add mocks for test view
        test_view.get_success_url = Mock(return_value='/')
        test_view.get_object =\
            Mock(return_value=test_customer)

        # call delete() and check that the success message has been added
        test_view.delete(generic_request)
        messages.success.assert_called()

    # get_success_message()
    def test_method_get_success_message_createview_success_message(self):
        view = DummySSMCreateView
        object_name = view.model.__name__
        self.assertEqual(
            view().get_success_message(self.cleaned_data_empty),
            f"{object_name} create {self.mixin.success_message}")

    def test_method_get_success_message_updateview_success_message(self):
        view = DummySSMUpdateView
        object_name = view.model.__name__
        self.assertEqual(
            view().get_success_message(self.cleaned_data_empty),
            f"{object_name} update {self.mixin.success_message}")

    def test_method_get_success_message_deleteview_success_message(self):
        view = DummySSMDeleteView
        object_name = view.model.__name__
        self.assertEqual(
            view().get_success_message(self.cleaned_data_empty),
            f"{object_name} delete {self.mixin.success_message}")


# dummy mixin is used to avoid duplicate boilerplate in dummy views
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
        cls.mixin = mixins.CommonViewMixin

    def test_attribute_context_object_name_value(self):
        self.assertEqual(self.mixin.context_object_name, 'object')

    # get_context_data()
    def test_context_has_action_verb_none_in_templateview(self):
        class DummyTemplateView(self.mixin, TemplateView):
            pass

        self.dummy_templateview = DummyTemplateView()
        self.dummy_templateview.setup(generic_request)

        context = self.dummy_templateview.get_context_data()
        self.assertEqual(context['action_verb'], None)

    def test_context_has_action_verb_create_in_createview(self):
        class DummyCreateView(self.mixin, DummyMixin, CreateView):
            pass

        self.dummy_createview = DummyCreateView()
        self.dummy_createview.setup(generic_request)

        context = self.dummy_createview.get_context_data()
        self.assertEqual(context['action_verb'], 'create')

    def test_context_has_action_verb_create_in_updateview(self):
        class DummyUpdateView(self.mixin, DummyMixin, UpdateView):
            pass

        self.dummy_updateview = DummyUpdateView()
        self.dummy_updateview.setup(generic_request)

        context = self.dummy_updateview.get_context_data()
        self.assertEqual(context['action_verb'], 'update')

    # get_success_url
    def test_method_get_success_url_returns_expected_url(self):
        # create an instance of the mixin using the Customer model
        mixin_instance = self.mixin()
        mixin_instance.model = Customer
        success_url = mixin_instance.get_success_url()

        # success_url
        self.assertEqual(success_url, reverse('stripes:customer_list'))


# CustomerViewMixin
class DummyCVMCreateView(mixins.CustomerViewMixin, CreateView):
    model = AbstractModel


class DummyCVMUpdateView(mixins.CustomerViewMixin, UpdateView):
    model = AbstractModel


class CustomerViewMixinTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.mixin = mixins.CustomerViewMixin

    def test_attribute_model_name_value(self):
        self.assertEqual(self.mixin.model, Customer)

    def test_attribute_pk_url_kwarg_value(self):
        self.assertEqual(self.mixin.pk_url_kwarg, 'customer_pk')

    # dispatch()
    def test_method_dispatch_returns_expected_value_for_createview(self):
        view_instance = DummyCVMCreateView()
        view_instance.setup(generic_request)
        view_instance.dispatch(generic_request)
        self.assertEqual(view_instance.fields, ())

    def test_method_dispatch_returns_expected_value_for_updateview(self):
        view_instance = DummyCVMUpdateView()
        view_instance.setup(generic_request)
        view_instance.get_object = Mock(return_value=None)
        view_instance.dispatch(generic_request)
        self.assertEqual(view_instance.fields, '__all__')


# PaymentMethodViewMixin
class DummyPVMCreateView(mixins.PaymentMethodViewMixin, CreateView):
    model = AbstractModel


class DummyPVMUpdateView(mixins.PaymentMethodViewMixin, UpdateView):
    model = AbstractModel


class PaymentMethodViewMixinTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.mixin = mixins.PaymentMethodViewMixin

    def test_attribute_model_name_value(self):
        self.assertEqual(self.mixin.model, PaymentMethod)

    def test_attribute_pk_url_kwarg_value(self):
        self.assertEqual(self.mixin.pk_url_kwarg, 'paymentmethod_pk')

    # dispatch()
    def test_method_dispatch_returns_expected_value_for_createview(self):
        view_instance = DummyPVMCreateView()
        view_instance.setup(generic_request)
        view_instance.dispatch(generic_request)
        self.assertEqual(view_instance.fields, ())

    def test_method_dispatch_returns_expected_value_for_updateview(self):
        view_instance = DummyPVMUpdateView()
        view_instance.setup(generic_request)
        view_instance.get_object = Mock(return_value=None)
        view_instance.dispatch(generic_request)
        self.assertEqual(view_instance.fields, '__all__')
