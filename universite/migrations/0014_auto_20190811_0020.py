# Generated by Django 2.2.3 on 2019-08-11 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('universite', '0013_ingredient_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facult',
            name='programoffer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='programs', to='universite.Program'),
        ),
        migrations.AlterField(
            model_name='facult',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='universites', to='universite.University'),
        ),
        migrations.AlterField(
            model_name='program',
            name='university',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='universite', to='universite.University'),
        ),
    ]
