# Generated by Django 4.1.2 on 2022-11-17 21:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_movimento_data_alter_movimento_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimento',
            name='data',
            field=models.DateField(default=datetime.datetime(2022, 11, 17, 18, 44, 13, 443817)),
        ),
    ]