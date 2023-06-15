# Generated by Django 3.2.19 on 2023-06-15 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='ad',
            index=models.Index(fields=['url'], name='ad_url_idx'),
        ),
        migrations.AddIndex(
            model_name='ad',
            index=models.Index(fields=['is_sent'], name='ad_is_sent_idx'),
        ),
        migrations.AddIndex(
            model_name='ad',
            index=models.Index(fields=['created_at'], name='ad_created_at_idx'),
        ),
    ]