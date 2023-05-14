# Generated by Django 4.2 on 2023-04-30 16:09

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mountain_huts', '0016_alter_mountainhut_email_alter_mountainhut_position_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mountainhut',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hut_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mountainhut',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mountainhut',
            name='position',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='mountainhut',
            name='subtitle',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='mountainhut',
            name='telephone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='mountainhut',
            name='text',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='mountainhut',
            name='website',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]