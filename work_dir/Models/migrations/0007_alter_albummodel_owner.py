# Generated by Django 3.2.16 on 2023-03-26 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0006_alter_imagemodel_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='albummodel',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='Models.model'),
        ),
    ]
