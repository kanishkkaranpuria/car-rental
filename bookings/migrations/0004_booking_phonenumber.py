# Generated by Django 3.2.8 on 2022-04-25 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0003_auto_20220425_0532'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='phoneNumber',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
