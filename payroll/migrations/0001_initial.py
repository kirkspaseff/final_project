# Generated by Django 3.2.7 on 2021-11-02 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofile', '0008_auto_20211101_2105'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_period_start', models.DateField()),
                ('pay_period_end', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.employee')),
            ],
        ),
        migrations.AddConstraint(
            model_name='payroll',
            constraint=models.UniqueConstraint(fields=('employee', 'pay_period_end'), name='unique_pay_period'),
        ),
    ]
