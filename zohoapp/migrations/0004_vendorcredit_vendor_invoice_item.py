# Generated by Django 4.1.7 on 2023-06-27 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0003_yourmodel_remove_vendorcreditinvoice_inv_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='VendorCredit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_id', models.TextField(max_length=255)),
                ('vendor_email', models.CharField(max_length=250)),
                ('gst_treatment', models.CharField(max_length=100)),
                ('source_supply', models.CharField(max_length=100)),
                ('baddress', models.CharField(default='', max_length=300)),
                ('credit_note', models.CharField(blank=True, max_length=100, null=True)),
                ('order_no', models.CharField(blank=True, max_length=100, null=True)),
                ('vendor_date', models.DateField()),
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
            ],
        ),
        migrations.CreateModel(
            name='Vendor_invoice_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.TextField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('hsn', models.TextField(max_length=255)),
                ('tax', models.IntegerField()),
                ('total', models.FloatField()),
                ('discount', models.TextField(max_length=255)),
                ('rate', models.TextField(max_length=255)),
                ('inv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.invoice')),
            ],
        ),
    ]
