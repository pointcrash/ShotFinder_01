# Generated by Django 3.2.16 on 2023-03-26 17:24

import Photographers.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumPh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Альбом', max_length=255)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShootingGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=250, null=True, verbose_name='Город')),
                ('age', models.PositiveSmallIntegerField(null=True, verbose_name='Возраст')),
                ('gender', models.CharField(choices=[('M', 'Мужской'), ('F', 'Женский'), ('O', 'Другое')], default='M', max_length=1, verbose_name='Пол')),
                ('about', models.TextField(null=True, verbose_name='О себе')),
                ('in_under_photos', models.BooleanField(default=False, verbose_name='Согласие на фото в нижнем белье/купальнике')),
                ('nu_photos', models.BooleanField(default=False, verbose_name='Согласие на ню-фото (18+)')),
                ('tfp_photos', models.BooleanField(default=False, null=True, verbose_name='Сотрудничество по ТФП')),
                ('avatar', models.ImageField(blank=True, upload_to='avatar/ph/%Y/%m/%d/', verbose_name='Фото профиля')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовать')),
                ('inst', models.CharField(max_length=50, null=True)),
                ('vk', models.CharField(max_length=250, null=True)),
                ('tg', models.CharField(max_length=50, null=True)),
                ('genre', models.ManyToManyField(to='Photographers.ShootingGenre')),
                ('like', models.ManyToManyField(blank=True, related_name='likes_ph', to=settings.AUTH_USER_MODEL)),
                ('owner', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ImagePh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=Photographers.models.user_directory_path)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image_ph', to='Photographers.albumph')),
                ('model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='Photographers.photographer')),
            ],
        ),
        migrations.CreateModel(
            name='CommentPh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, null=True)),
                ('text', models.TextField(null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('asshole', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Photographers.photographer')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='albumph',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='Photographers.photographer'),
        ),
    ]
