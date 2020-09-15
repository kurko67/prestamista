# Generated by Django 2.2.11 on 2020-08-18 00:56

from django.db import migrations, models
import loans.models


class Migration(migrations.Migration):

    dependencies = [
        ('loans', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='status',
            field=models.CharField(choices=[(loans.models.OrderStatus('CREATED'), 'CREATED'), (loans.models.OrderStatus('PAYED'), 'PAYED'), (loans.models.OrderStatus('LEGAL'), 'LEGAL')], default='CREATED', max_length=50),
        ),
    ]
