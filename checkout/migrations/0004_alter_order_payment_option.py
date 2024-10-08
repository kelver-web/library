# Generated by Django 4.1.3 on 2024-09-22 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_alter_order_payment_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_option',
            field=models.CharField(choices=[('deposito', 'Depósito'), ('pagseguro', 'PagSeguro'), ('paypal', 'Paypal')], default='deposito', max_length=20, verbose_name='Opção de Pagamento'),
        ),
    ]
