# Generated by Django 3.2.19 on 2023-05-18 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_auto_20230516_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='url',
            field=models.URLField(),
        ),
    ]
