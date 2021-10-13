# Generated by Django 3.2.7 on 2021-10-13 03:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('barcodes', '0002_alter_barcode_barcode'),
        ('sellby', '0002_alter_record_expirydate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='isRemoved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterUniqueTogether(
            name='record',
            unique_together={('barcode', 'user', 'expiryDate')},
        ),
    ]