# Generated by Django 3.2.9 on 2021-12-04 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_planes_usuario_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opciones',
            name='diapositivos_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.diapositivos'),
        ),
        migrations.AlterField(
            model_name='valvula',
            name='diapositivos_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.diapositivos'),
        ),
    ]