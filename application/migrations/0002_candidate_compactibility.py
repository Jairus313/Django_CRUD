# Generated by Django 3.0.2 on 2020-05-30 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='compactibility',
            field=models.IntegerField(default='0'),
        ),
    ]
