# Generated by Django 4.1 on 2022-08-25 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Wallet', '0004_remove_transaction_receipt_receipt_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet',
            name='currency',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
