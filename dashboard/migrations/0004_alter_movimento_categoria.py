# Generated by Django 4.1.2 on 2022-11-09 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_movimento_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimento',
            name='categoria',
            field=models.CharField(max_length=50),
        ),
    ]
