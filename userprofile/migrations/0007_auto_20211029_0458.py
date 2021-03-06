# Generated by Django 3.2.7 on 2021-10-29 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0006_auto_20211017_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='city',
            field=models.CharField(blank=True, max_length=75, null=True, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Telephone Number'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='postal_code',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Postal Code'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='state',
            field=models.CharField(blank=True, max_length=2, null=True, verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='street',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Street Address'),
        ),
    ]
