# Generated by Django 3.2.8 on 2022-04-25 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.EmailField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='booking',
            name='name',
            field=models.CharField(default='', max_length=250),
        ),
    ]
