# Generated by Django 5.0.2 on 2024-12-24 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_alter_admin_phone_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='name',
        ),
    ]
