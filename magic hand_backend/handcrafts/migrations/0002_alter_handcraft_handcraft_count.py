# Generated by Django 5.0.2 on 2024-12-24 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handcrafts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='handcraft',
            name='handcraft_count',
            field=models.IntegerField(),
        ),
    ]
