# Generated by Django 5.1.3 on 2024-11-29 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PerformanceCars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelName', models.CharField(max_length=225)),
                ('brand', models.CharField(max_length=225)),
                ('engine', models.CharField(max_length=225)),
                ('horsepower', models.IntegerField()),
                ('torque', models.IntegerField()),
                ('acceleration', models.IntegerField()),
            ],
        ),
    ]
