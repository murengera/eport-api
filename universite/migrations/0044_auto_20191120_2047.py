# Generated by Django 2.2.6 on 2019-11-20 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('universite', '0043_auto_20191120_1815'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='university',
            options={'ordering': ('-name',)},
        ),
        migrations.RemoveField(
            model_name='university',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='university',
            name='key_person',
        ),
    ]