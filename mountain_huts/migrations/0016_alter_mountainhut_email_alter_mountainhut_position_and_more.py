# Generated by Django 4.2 on 2023-04-30 16:00

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('mountain_huts', '0015_rename_parent_mountainhut_region_mountainhut_gebirge_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mountainhut',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='mountainhut',
            name='position',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='mountainhut',
            name='rating',
            field=models.CharField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=1),
        ),
        migrations.AlterField(
            model_name='mountainhut',
            name='subtitle',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='mountainhut',
            name='telephone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='mountainhut',
            name='text',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='mountainhut',
            name='website',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
