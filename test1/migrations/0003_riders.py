# Generated by Django 4.1.4 on 2022-12-20 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0002_requester'),
    ]

    operations = [
        migrations.CreateModel(
            name='Riders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromLocation', models.CharField(max_length=255)),
                ('toLocation', models.CharField(max_length=255)),
                ('dateTime', models.DateTimeField()),
                ('flexibleTimings', models.BooleanField()),
                ('numberOfAssets', models.IntegerField()),
                ('travelMedium', models.CharField(choices=[('BUS', 'BUS'), ('CAR', 'CAR'), ('TRAIN', 'TRAIN')], max_length=255)),
                ('status', models.CharField(choices=[('APPLIED', 'APPLIED'), ('NOTAPPLIED', 'NOTAPPLIED')], max_length=255)),
                ('acceptedPersonDetails', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
