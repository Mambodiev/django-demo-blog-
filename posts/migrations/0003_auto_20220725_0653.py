# Generated by Django 2.2.1 on 2022-07-25 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['last_updated']},
        ),
        migrations.AddField(
            model_name='post',
            name='post_capital',
            field=models.CharField(default='T', max_length=1),
        ),
    ]
