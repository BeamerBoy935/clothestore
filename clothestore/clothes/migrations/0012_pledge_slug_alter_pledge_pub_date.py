# Generated by Django 4.1 on 2022-08-10 14:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0011_pledge_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='pledge',
            name='slug',
            field=models.SlugField(default=None),
        ),
        migrations.AlterField(
            model_name='pledge',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 8, 10, 14, 48, 21, 479000, tzinfo=datetime.timezone.utc)),
        ),
    ]
