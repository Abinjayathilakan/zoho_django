# Generated by Django 4.1.7 on 2023-06-29 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zohoapp', '0007_vendordemo_item_vendordemo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendorcredit',
            name='customer',
        ),
        migrations.AddField(
            model_name='vendorcredit',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]