# Generated by Django 3.2.9 on 2021-12-05 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20211204_1603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='errores',
            old_name='tipo',
            new_name='titulo',
        ),
    ]
