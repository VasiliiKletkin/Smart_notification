# Generated by Django 3.2.19 on 2023-05-14 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_ticket_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='telegram_id',
            field=models.CharField(default=1, max_length=30, verbose_name='Telegram'),
            preserve_default=False,
        ),
    ]
