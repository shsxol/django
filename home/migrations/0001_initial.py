# Generated by Django 4.1.4 on 2022-12-26 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='media')),
                ('rank', models.IntegerField(null=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='media')),
                ('description', models.TextField(blank=True)),
                ('slug', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.CharField(max_length=100)),
                ('slug', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='media')),
                ('rank', models.IntegerField(null=True)),
                ('url', models.URLField(max_length=500)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.TextField(unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('discounted_price', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='media')),
                ('description', models.TextField(blank=True)),
                ('specification', models.TextField(blank=True)),
                ('slug', models.TextField(unique=True)),
                ('stock', models.CharField(choices=[('in stock', 'in stock'), ('out of stock', 'out of stock')], max_length=100)),
                ('label', models.CharField(blank=True, choices=[('hot', 'hot'), ('new', 'new'), ('sale', 'sale'), ('', 'default')], max_length=100)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.subcategory')),
            ],
        ),
    ]