# Generated by Django 3.2.10 on 2022-04-30 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='policy',
            name='roomtype',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='policy',
            name='tenure',
            field=models.CharField(max_length=1000),
        ),
    ]
