# Generated by Django 3.2 on 2023-05-19 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ManyBrowzers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('browzers', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ManyCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Manylanguages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languages', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ManyTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Turi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languages', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date1', models.DateField()),
                ('username', models.CharField(max_length=255)),
                ('img', models.ImageField(blank=True, default='img/img.jpg', null=True, upload_to='img/')),
                ('down', models.FileField(upload_to='media')),
                ('life', models.CharField(max_length=255)),
                ('resolution', models.BooleanField(default=False)),
                ('date2', models.DateField()),
                ('github', models.CharField(max_length=255)),
                ('layout', models.BooleanField(default=False)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('browsers', models.ManyToManyField(blank=True, to='backend.ManyBrowzers')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.manycategory')),
                ('languages', models.ManyToManyField(blank=True, to='backend.Manylanguages')),
                ('tags', models.ManyToManyField(blank=True, to='backend.ManyTags')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('languages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.turi')),
            ],
        ),
    ]
