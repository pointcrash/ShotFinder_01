# Generated by Django 3.2.16 on 2023-04-14 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0010_alter_model_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='inst',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='model',
            name='tfp_photos',
            field=models.BooleanField(default=False, verbose_name='Сотрудничество по ТФП'),
        ),
        migrations.AlterField(
            model_name='model',
            name='tg',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='model',
            name='vk',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]