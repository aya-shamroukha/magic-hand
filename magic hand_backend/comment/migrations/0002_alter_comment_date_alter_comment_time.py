# Generated by Django 5.0.2 on 2024-12-27 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
