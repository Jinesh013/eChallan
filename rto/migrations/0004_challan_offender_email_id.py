# Generated by Django 4.1.5 on 2023-03-15 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rto', '0003_challan'),
    ]

    operations = [
        migrations.AddField(
            model_name='challan',
            name='offender_email_id',
            field=models.CharField(default=None, max_length=25),
        ),
    ]
