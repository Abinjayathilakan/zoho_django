# Generated by Django 4.1.7 on 2023-07-08 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0014_credits_doc_upload_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor_credits',
            name='adjustment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
