# Generated by Django 2.2.3 on 2019-08-11 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('universite', '0018_auto_20190811_0105'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='university',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='universities', to='universite.University'),
        ),
    ]
