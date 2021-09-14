from django.contrib import messages
from django.test import RequestFactory, TestCase
from django.urls import reverse
from django.views.generic import CreateView, DeleteView, TemplateView,\
    UpdateView
from unittest.mock import Mock, patch

from .mixins import StripeCommonViewMixin, CustomerViewMixin,\
                    PaymentMethodViewMixin, StripeSuccessMessageMixin
from .models import AbstractModel, Customer, PaymentMethod

generic_request = RequestFactory().get('/')


# StripeSuccessMessageMixin
class DummySSMCreateView(StripeSuccessMessageMixin, CreateView):
    model = AbstractModel


class DummySSMUpdateView(StripeSuccessMessageMixin, UpdateView):
    model = AbstractModel


class DummySSMDeleteView(StripeSuccessMessageMixin, DeleteView):
    model = AbstractModel


class StripeSuccessMessageMixinTest(TestCase):
    stub_cleaned_data = {}

    @classmethod
    def setUpTestData(cls):
        cls.mixin = StripeSuccessMessageMixin

    def test_attribute_value_success_message(self):
        self.assertEqual(self.mixin.success_message, 'success')

    # delete()
    @patch('django.contrib.messages.success', Mock(return_value=True))
    def test_method_delete_calls_function_messages_success_old(self):
        view_instance = DummySSMDeleteView()
        view_instance.setup(generic_request)

        # add mocks to satisfy delete() method
        view_instance.get_success_url = Mock(return_value='/')
        view_instance.get_object = Mock()

        # call delete() and check that messages.success has been called
        view_instance.delete(generic_request)
        messages.success.assert_called()

    # get_success_message()
    def test_method_get_success_message_createview_success_message(self):
        view = DummySSMCreateView
        object_name = view.model.__name__
        self.assertEqual(
            view().get_success_message(self.stub_cleaned_data),
            f"{object_name} create {self.mixin.success_message}")

    def test_method_get_success_message_updateview_success_message(self):
        view = DummySSMUpdateView
        object_name = view.model.__name__
        self.assertEqual(
            view().get_success_message(self.stub_cleaned_data),
            f"{object_name} update {self.mixin.success_message}")

    def test_method_get_success_message_deleteview_success_message(self):
        view = DummySSMDeleteView
        object_name = view.model.__name__
        self.assertEqual(
            view().get_success_message(self.stub_cleaned_data),
            f"{object_name} delete {self.mixin.success_message}")


# StripeCommonViewMixin
class DummySCVMTemplateView(StripeCommonViewMixin, TemplateView):
    model = AbstractModel


class DummySCVMCreateView(StripeCommonViewMixin, CreateView):
    model = AbstractModel


class DummySCVMUpdateView(StripeCommonViewMixin, UpdateView):
    model = AbstractModel


class StripeCommonViewMixinTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.mixin = StripeCommonViewMixin

    def test_attribute_context_object_name_value(self):
        self.assertEqual(self.mixin.context_object_name, 'object')

    # dispatch()
    def test_method_dispatch_sets_expected_fields_for_createview(self):
        view_instance = DummySCVMCreateView()
        view_instance.setup(generic_request)

        view_instance.get = Mock(return_value=None)  # satisfies dispatch()
        view_instance.dispatch(generic_request)
        self.assertEqual(view_instance.fields, ())

    def test_method_dispatch_sets_expected_fields_for_updateview(self):
        view_instance = DummySCVMUpdateView()
        view_instance.setup(generic_request)

        view_instance.get = Mock(return_value=None)  # satisfies dispatch()
        view_instance.dispatch(generic_request)
        self.assertEqual(view_instance.fields, '__all__')

    # get_context_data()
    def test_context_has_action_verb_create_in_createview(self):
        view_instance = DummySCVMCreateView()
        view_instance.setup(generic_request)

        view_instance.get_form = Mock()  # satisfies get_context_data()
        view_instance.object = Mock()  # satisfies get_context_data()

        context = view_instance.get_context_data()
        self.assertEqual(context['action_verb'], 'create')

    def test_context_has_action_verb_update_in_updateview(self):
        view_instance = DummySCVMUpdateView()
        view_instance.setup(generic_request)

        view_instance.get_form = Mock()  # satisfies get_context_data()
        view_instance.object = Mock()  # satisfies get_context_data()

        context = view_instance.get_context_data()
        self.assertEqual(context['action_verb'], 'update')

    def test_context_has_action_verb_none_in_non_create_or_update_view(self):
        view_instance = DummySCVMTemplateView()
        view_instance.setup(generic_request)

        # satisfies get_context_data()
        view_instance.get_queryset = Mock(return_value={})

        context = view_instance.get_context_data()
        self.assertEqual(context['action_verb'], None)

    # get_success_url
    def test_method_get_success_url_returns_expected_url(self):
        mixin_instance = self.mixin()
        mixin_instance.model = Customer
        success_url = mixin_instance.get_success_url()

        # success_url
        self.assertEqual(success_url, reverse('stripes:customer_list'))


# CustomerViewMixin
class DummyCVMCreateView(CustomerViewMixin, CreateView):
    model = AbstractModel


class DummyCVMUpdateView(CustomerViewMixin, UpdateView):
    model = AbstractModel


class CustomerViewMixinTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.mixin = CustomerViewMixin

    def test_attribute_model_name_value(self):
        self.assertEqual(self.mixin.model, Customer)

    def test_attribute_pk_url_kwarg_value(self):
        self.assertEqual(self.mixin.pk_url_kwarg, 'customer_pk')


# PaymentMethodViewMixin
class DummyPVMCreateView(PaymentMethodViewMixin, CreateView):
    model = AbstractModel


class DummyPVMUpdateView(PaymentMethodViewMixin, UpdateView):
    model = AbstractModel


class PaymentMethodViewMixinTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.mixin = PaymentMethodViewMixin

    def test_attribute_model_name_value(self):
        self.assertEqual(self.mixin.model, PaymentMethod)

    def test_attribute_pk_url_kwarg_value(self):
        self.assertEqual(self.mixin.pk_url_kwarg, 'paymentmethod_pk')
