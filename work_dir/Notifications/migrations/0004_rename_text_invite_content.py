# Generated by Django 3.2.16 on 2023-04-15 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Notifications', '0003_alter_invite_unique_together'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invite',
            old_name='text',
            new_name='content',
        ),
    ]
