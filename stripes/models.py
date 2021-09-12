from django.db import models


class AbstractModel(models.Model):
    def get_absolute_url(self):
        return '/'

    def __str__(self):
        return str(self.id)


# class Coupon(models.Model):
#     stripe_coupon = models.JSONField(blank=True, null=True)


class Customer(AbstractModel):
    stripe_customer = models.JSONField(blank=True, null=True)


# class Discount(models.Model):
#     stripe_discount = models.JSONField(blank=True, null=True)


# class Dispute(models.Model):
#     stripe_dispute = models.JSONField(blank=True, null=True)


# class Invoice(models.Model):
#     stripe_invoice = models.JSONField(blank=True, null=True)


# class Order(models.Model):
#     stripe_order = models.JSONField(blank=True, null=True)


# class Price(models.Model):
#     stripe_price = models.JSONField(blank=True, null=True)


# class Plan(models.Model):
#     stripe_plan = models.JSONField(blank=True, null=True)


# class Product(models.Model):
#     stripe_product = models.JSONField(blank=True, null=True)


# class PaymentIntent(models.Model):
#     stripe_payment_intent = models.JSONField(blank=True, null=True)


# class PaymentMethod(models.Model):
#     stripe_payment_method = models.JSONField(blank=True, null=True)


# class Quote(models.Model):
#     stripe_quote = models.JSONField(blank=True, null=True)


# class Refund(models.Model):
#     stripe_refund = models.JSONField(blank=True, null=True)


# class Session(models.Model):
#     stripe_session = models.JSONField(blank=True, null=True)


# class SetupIntent(models.Model):
#     stripe_setup_intent = models.JSONField(blank=True, null=True)


# class Sku(models.Model):
#     stripe_sku = models.JSONField(blank=True, null=True)


# class Subscription(models.Model):
#     stripe_subscription = models.JSONField(blank=True, null=True)


# class TaxRate(models.Model):
#     stripe_tax_rate = models.JSONField(blank=True, null=True)
