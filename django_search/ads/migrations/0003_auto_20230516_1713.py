# Generated by Django 3.2.19 on 2023-05-16 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_auto_20230516_1701'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ad',
            options={'verbose_name': 'Ad', 'verbose_name_plural': 'Ads'},
        ),
        migrations.AlterField(
            model_name='ad',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
