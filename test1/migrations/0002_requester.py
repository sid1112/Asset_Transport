# Generated by Django 4.1.4 on 2022-12-20 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requester',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromLocation', models.CharField(max_length=255)),
                ('toLocation', models.CharField(max_length=255)),
                ('dateTime', models.DateTimeField()),
                ('flexibleTimings', models.BooleanField()),
                ('numberOfAssets', models.IntegerField()),
                ('assetType', models.CharField(choices=[('LAPTOP', 'LAPTOP'), ('TRAVEL_BAG', 'TRAVEL_BAG'), ('PACKAGE', 'PACKAGE')], max_length=255)),
                ('assetSensitivity', models.CharField(choices=[('HIGHLY_SENSITIVE', 'HIGHLY_SENSITIVE'), ('SENSITIVE', 'SENSITIVE'), ('NORMAL', 'NORMAL')], max_length=255)),
                ('whomToDeliver', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('CONFIRM', 'CONFIRM'), ('PENDING', 'PENDING'), ('EXPIRED', 'EXPIRED')], max_length=255)),
            ],
        ),
    ]
