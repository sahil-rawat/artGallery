# Generated by Django 3.2 on 2021-04-29 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtGallery', '0002_alter_art_salestatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='saleStatus',
            field=models.BooleanField(db_column='status'),
        ),
    ]