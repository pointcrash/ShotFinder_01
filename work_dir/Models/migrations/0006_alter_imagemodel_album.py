# Generated by Django 3.2.16 on 2023-03-25 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0005_auto_20230325_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='album', to='Models.albummodel'),
        ),
    ]
