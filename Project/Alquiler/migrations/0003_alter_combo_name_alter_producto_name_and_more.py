# Generated by Django 4.2.5 on 2024-01-15 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alquiler', '0002_tipocombo_combo_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='combo',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='producto',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='tipocombo',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]
