# Generated by Django 3.2 on 2022-07-27 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_content_overview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
