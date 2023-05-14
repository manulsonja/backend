# Generated by Django 4.2 on 2023-04-18 19:47

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import pictures.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', pictures.models.PictureField(aspect_ratios=[None], breakpoints={'l': 1200, 'm': 992, 's': 768, 'xl': 1400, 'xs': 576}, container_width=1200, file_types=['JPEG'], grid_columns=12, pixel_densities=[1, 2], upload_to='')),
                ('toilet', models.BooleanField(null=True)),
                ('fees', models.FloatField(null=True)),
                ('name', models.CharField(max_length=30)),
                ('position', django.contrib.gis.db.models.fields.PointField(null=True, srid=4326)),
                ('parkingtype', models.CharField(choices=[('parkplatz', 'Parkplatz'), ('haltestelle', 'Haltestelle'), ('stellplatz', 'Stellplatz'), ('sonstige', 'Sonstige')], default='parkplatz', max_length=20)),
            ],
        ),
    ]