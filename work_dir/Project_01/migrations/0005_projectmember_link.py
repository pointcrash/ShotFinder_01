# Generated by Django 3.2.16 on 2023-04-02 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project_01', '0004_professions_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectmember',
            name='link',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
