# Generated by Django 3.2.16 on 2023-03-26 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0007_alter_albummodel_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album', to='Models.albummodel'),
        ),
    ]
