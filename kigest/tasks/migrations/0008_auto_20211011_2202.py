# Generated by Django 3.2.7 on 2021-10-11 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0004_remove_manager_tasks'),
        ('tasks', '0007_alter_task_assignee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assignee',
            field=models.ManyToManyField(related_name='assignee', to='userprofile.Employee'),
        ),
        migrations.AlterField(
            model_name='task',
            name='assigner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='userprofile.employee'),
        ),
    ]
