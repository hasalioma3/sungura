# Generated by Django 4.0.5 on 2022-06-13 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('barcode', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
            ],
        ),
    ]
