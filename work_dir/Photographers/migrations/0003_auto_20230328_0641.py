# Generated by Django 3.2.16 on 2023-03-28 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Photographers', '0002_rename_user_albumph_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentph',
            old_name='asshole',
            new_name='post',
        ),
        migrations.AlterField(
            model_name='commentph',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
