# Generated by Django 4.0.4 on 2022-11-06 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tornado', '0005_remove_tornado_date_remove_tornado_distance_covered_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tornado',
            name='tncategoria',
            field=models.CharField(default='Delitos Sexuales', max_length=50),
        ),
    ]
