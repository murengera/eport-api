# Generated by Django 2.2.3 on 2019-07-25 19:01

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondaryapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secondary',
            name='emails',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(blank=True, max_length=254), size=None),
        ),
    ]