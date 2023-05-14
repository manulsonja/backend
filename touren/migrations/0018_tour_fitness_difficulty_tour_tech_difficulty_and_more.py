# Generated by Django 4.2 on 2023-05-09 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('touren', '0017_tour_offseason'),
    ]

    operations = [
        migrations.AddField(
            model_name='tour',
            name='fitness_difficulty',
            field=models.CharField(choices=[('leicht', 'LEICHT'), ('mittel', 'MITTEL'), ('schwierig', 'SCHWIERIG')], default='schwierig', max_length=10),
        ),
        migrations.AddField(
            model_name='tour',
            name='tech_difficulty',
            field=models.CharField(choices=[('leicht', 'LEICHT'), ('mittel', 'MITTEL'), ('schwierig', 'SCHWIERIG')], default='schwierig', max_length=10),
        ),
        migrations.AlterField(
            model_name='tour',
            name='difficulty',
            field=models.CharField(choices=[('leicht', 'LEICHT'), ('mittel', 'MITTEL'), ('schwierig', 'SCHWIERIG')], default='schwierig', editable=False, max_length=10),
        ),
    ]