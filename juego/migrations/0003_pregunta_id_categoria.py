# Generated by Django 3.2.6 on 2021-09-03 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('juego', '0002_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='pregunta',
            name='id_categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='juego.categoria'),
            preserve_default=False,
        ),
    ]
