# Generated by Django 5.0.2 on 2025-03-10 17:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('handcrafts', '0003_handcraft_handcraft_cost'),
        ('maker', '0003_remove_maker_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.TextField()),
                ('description', models.TextField()),
                ('from_date', models.DateTimeField(auto_now_add=True)),
                ('to_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='AuctionHandcraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction.auction')),
                ('handcraft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='handcrafts.handcraft')),
            ],
        ),
        migrations.CreateModel(
            name='MakerAuction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction.auction')),
                ('maker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maker.maker')),
            ],
        ),
    ]
