# Generated by Django 3.2.9 on 2021-11-15 11:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0002_auto_20211115_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaveprocess',
            name='leave_days',
        ),
        migrations.AddField(
            model_name='leaveprocess',
            name='end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='leaveprocess',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
