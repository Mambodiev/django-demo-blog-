# Generated by Django 2.2.1 on 2022-07-26 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20220725_0653'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
