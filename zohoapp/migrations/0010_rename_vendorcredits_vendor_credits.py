# Generated by Django 4.1.7 on 2023-06-30 06:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zohoapp', '0009_vendor_invoice_items_vendorcredits_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='VendorCredits',
            new_name='Vendor_Credits',
        ),
    ]