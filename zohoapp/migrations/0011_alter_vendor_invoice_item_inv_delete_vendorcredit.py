# Generated by Django 4.1.7 on 2023-07-01 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0010_rename_vendorcredits_vendor_credits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor_invoice_item',
            name='inv',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zohoapp.vendor_credits'),
        ),
        migrations.DeleteModel(
            name='VendorCredit',
        ),
    ]
