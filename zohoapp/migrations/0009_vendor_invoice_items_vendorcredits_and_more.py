# Generated by Django 4.1.7 on 2023-06-30 06:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zohoapp', '0008_remove_vendorcredit_customer_vendorcredit_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor_invoice_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.TextField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('hsn', models.TextField(max_length=255)),
                ('tax', models.IntegerField()),
                ('total', models.FloatField()),
                ('discount', models.TextField(max_length=255)),
                ('rate', models.TextField(max_length=255)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VendorCredits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=150)),
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
                ('status', models.TextField(max_length=255)),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='vendordemo_item',
            name='inv',
        ),
        migrations.RemoveField(
            model_name='vendorcredit',
            name='vendor_id',
        ),
        migrations.AddField(
            model_name='vendorcredit',
            name='company_name',
            field=models.CharField(default=2, max_length=150),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='VendorDemo',
        ),
        migrations.DeleteModel(
            name='VendorDemo_item',
        ),
    ]
