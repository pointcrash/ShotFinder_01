# Generated by Django 3.2.16 on 2023-04-14 10:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatgroup',
            name='members',
            field=models.ManyToManyField(related_name='chat_group', to=settings.AUTH_USER_MODEL),
        ),
    ]