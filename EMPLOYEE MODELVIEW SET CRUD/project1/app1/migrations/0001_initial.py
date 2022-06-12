# Generated by Django 4.0.4 on 2022-04-26 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('eid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('salary', models.FloatField()),
                ('address', models.CharField(max_length=100)),
                ('picture', models.ImageField(blank=True, upload_to='picture')),
            ],
        ),
    ]
