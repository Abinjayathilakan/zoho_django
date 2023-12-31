# Generated by Django 4.1.7 on 2023-06-29 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0006_vendor_invoice_item_delete_yourmodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorDemo_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.TextField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('hsn', models.TextField(max_length=255)),
                ('tax', models.IntegerField()),
                ('total', models.FloatField()),
                ('desc', models.TextField(max_length=255)),
                ('rate', models.TextField(max_length=255)),
                ('inv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.invoice')),
            ],
        ),
        migrations.CreateModel(
            name='VendorDemo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.TextField(max_length=255)),
                ('order_no', models.IntegerField()),
                ('inv_date', models.DateField()),
                ('due_date', models.DateField()),
                ('igst', models.TextField(max_length=255)),
                ('cgst', models.TextField(max_length=255)),
                ('sgst', models.TextField(max_length=255)),
                ('t_tax', models.FloatField()),
                ('subtotal', models.FloatField()),
                ('grandtotal', models.FloatField()),
                ('cxnote', models.TextField(max_length=255)),
                ('file', models.ImageField(upload_to='documents')),
                ('terms_condition', models.TextField(max_length=255)),
                ('status', models.TextField(max_length=255)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.customer')),
                ('terms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.payment_terms')),
            ],
        ),
    ]
