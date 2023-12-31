# Generated by Django 4.2.3 on 2023-12-23 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motorcycle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='motorcycle',
            name='year',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='motorcycle',
            name='brand',
            field=models.CharField(default='N/A', max_length=100),
        ),
        migrations.AlterField(
            model_name='motorcycle',
            name='id',
            field=models.AutoField(default='N/A', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='motorcycle',
            name='max_speed',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='motorcycle',
            name='model',
            field=models.CharField(default='N/A', max_length=100),
        ),
    ]
