# Generated by Django 4.1 on 2022-08-25 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Wallet', '0002_rename_customer_id_reward_customer_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='wallet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Wallet.wallet'),
        ),
    ]
