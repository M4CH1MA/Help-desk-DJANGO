# Generated by Django 5.0.3 on 2024-03-22 22:34

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chamado',
            name='show',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='chamado',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
