# Generated by Django 3.2.7 on 2021-09-30 23:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0002_alter_task_date_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='assigner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='manager', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='assignee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to=settings.AUTH_USER_MODEL),
        ),
    ]