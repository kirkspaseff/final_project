# Generated by Django 3.2.7 on 2021-10-08 02:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0003_auto_20211008_0152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='tasks',
        ),
    ]