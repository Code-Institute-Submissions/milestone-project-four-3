# Generated by Django 2.2.5 on 2020-05-20 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('era', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
                ('created_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('starting_price', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('buyout_price', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('status', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('current_bid', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
                ('current_bid_user', models.CharField(max_length=100, null=True)),
                ('current_bid_date', models.DateTimeField(null=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]
