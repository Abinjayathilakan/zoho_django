# Generated by Django 4.1.7 on 2023-06-29 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0005_delete_vendor_invoice_item'),
    ]

    operations = [
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
        migrations.DeleteModel(
            name='YourModel',
        ),
        migrations.RemoveField(
            model_name='vendorcredit',
            name='terms_condition',
        ),
    ]
