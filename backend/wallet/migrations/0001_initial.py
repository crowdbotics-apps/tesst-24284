# Generated by Django 2.2.18 on 2021-02-04 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task', '0001_initial'),
        ('task_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerWallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField()),
                ('expiration_date', models.DateTimeField()),
                ('last_transaction', models.DateTimeField()),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customerwallet_customer', to='task_profile.CustomerProfile')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_token', models.CharField(max_length=255)),
                ('payment_account', models.CharField(max_length=10)),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paymentmethod_wallet', to='wallet.CustomerWallet')),
            ],
        ),
        migrations.CreateModel(
            name='TaskerWallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField(max_length=254)),
                ('expiration_date', models.DateTimeField()),
                ('last_transaction', models.DateTimeField()),
                ('tasker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='taskerwallet_tasker', to='task_profile.TaskerProfile')),
            ],
        ),
        migrations.CreateModel(
            name='TaskerPaymentAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_token', models.CharField(max_length=255)),
                ('payment_account', models.CharField(max_length=10)),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taskerpaymentaccount_wallet', to='wallet.TaskerWallet')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('tip', models.FloatField()),
                ('tracking_id', models.CharField(max_length=50)),
                ('timestamp_created', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='paymenttransaction_customer', to='task_profile.CustomerProfile')),
                ('payment_method', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='paymenttransaction_payment_method', to='wallet.PaymentMethod')),
                ('tasker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='paymenttransaction_tasker', to='task_profile.TaskerProfile')),
                ('transaction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='paymenttransaction_transaction', to='task.TaskTransaction')),
            ],
        ),
    ]
