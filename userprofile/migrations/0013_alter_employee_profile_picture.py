# Generated by Django 3.2.7 on 2021-11-05 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0012_alter_employee_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile_picture',
            field=models.ImageField(blank=True, default='staticfiles/images/default.png', null=True, upload_to=''),
        ),
    ]