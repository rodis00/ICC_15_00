# Generated by Django 4.1.5 on 2023-01-17 17:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_client_email_alter_client_pesel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shift',
            name='worker',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='dateOfPurchase',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 17, 18, 38, 26, 175284), editable=False),
        ),
        migrations.AddField(
            model_name='shift',
            name='worker',
            field=models.ManyToManyField(to='App.worker'),
        ),
    ]
