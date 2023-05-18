# Generated by Django 4.2 on 2023-05-16 20:38

import ckeditor.fields
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок новости')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='ЧПУ')),
                ('description', ckeditor.fields.RichTextField(blank=True, verbose_name='Описание')),
                ('hide_description', models.BooleanField(default=False, verbose_name='Скрыть описание у постов')),
                ('is_published', models.BooleanField(default=True, verbose_name='Активность')),
                ('post_img1', models.ImageField(blank=True, null=True, upload_to='main/images/', verbose_name='Детальное фото 1')),
                ('post_img2', models.ImageField(blank=True, null=True, upload_to='main/images/', verbose_name='Детальное фото 2')),
                ('post_img3', models.ImageField(blank=True, null=True, upload_to='main/images/', verbose_name='Детальное фото 3')),
                ('post_img4', models.ImageField(blank=True, null=True, upload_to='main/images/', verbose_name='Детальное фото 4')),
                ('post_img5', models.ImageField(blank=True, null=True, upload_to='main/images/', verbose_name='Детальное фото 5')),
                ('post_img6', models.ImageField(blank=True, null=True, upload_to='main/images/', verbose_name='Детальное фото 6')),
                ('post_img7', models.ImageField(blank=True, null=True, upload_to='main/images/', verbose_name='Детальное фото 7')),
                ('post_img8', models.ImageField(blank=True, null=True, upload_to='main/images/', verbose_name='Детальное фото 8')),
                ('post_img9', models.ImageField(blank=True, null=True, upload_to='main/images/', verbose_name='Детальное фото 9')),
                ('post_img10', models.ImageField(blank=True, null=True, upload_to='main/images/', verbose_name='Детальное фото 10')),
                ('video_1', models.CharField(blank=True, max_length=300, verbose_name='Видео')),
                ('video_2', models.CharField(blank=True, max_length=300, verbose_name='Видео')),
                ('video_3', models.CharField(blank=True, max_length=300, verbose_name='Видео')),
                ('video_4', models.CharField(blank=True, max_length=300, verbose_name='Видео')),
                ('tags', taggit.managers.TaggableManager(help_text='Вводить через запятую', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Теги')),
            ],
            options={
                'verbose_name_plural': 'Посты',
            },
        ),
    ]