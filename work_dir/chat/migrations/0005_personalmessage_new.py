# Generated by Django 3.2.16 on 2023-04-21 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_personalmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalmessage',
            name='new',
            field=models.BooleanField(default=False),
        ),
    ]
