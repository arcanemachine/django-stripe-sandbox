# Generated by Django 3.2.7 on 2021-09-14 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stripes', '0005_auto_20210914_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmethod',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='paymentmethods', to='stripes.customer'),
        ),
    ]
