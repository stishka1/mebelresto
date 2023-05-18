from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField


# Create your models here.

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок новости')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    slug = models.SlugField('ЧПУ', max_length=100, db_index=True, unique=True)
    description = RichTextField(verbose_name='Описание', blank=True)
    hide_description = models.BooleanField(verbose_name='Скрыть описание', default=False)
    tags = TaggableManager(verbose_name="Теги", help_text="Вводить через запятую и пробел")
    is_published = models.BooleanField(verbose_name='Опубликован', default=True)
    post_img1 = models.ImageField(upload_to='main/images/', null=True, blank=True, max_length=100, verbose_name='Детальное фото 1')
    post_img2 = models.ImageField(upload_to='main/images/', null=True, blank=True, max_length=100, verbose_name='Детальное фото 2')
    post_img3 = models.ImageField(upload_to='main/images/', null=True, blank=True, max_length=100, verbose_name='Детальное фото 3')
    post_img4 = models.ImageField(upload_to='main/images/', null=True, blank=True, max_length=100, verbose_name='Детальное фото 4')
    post_img5 = models.ImageField(upload_to='main/images/', null=True, blank=True, max_length=100, verbose_name='Детальное фото 5')
    post_img6 = models.ImageField(upload_to='main/images/', null=True, blank=True, max_length=100, verbose_name='Детальное фото 6')
    post_img7 = models.ImageField(upload_to='main/images/', null=True, blank=True, max_length=100, verbose_name='Детальное фото 7')
    post_img8 = models.ImageField(upload_to='main/images/', null=True, blank=True, max_length=100, verbose_name='Детальное фото 8')
    post_img9 = models.ImageField(upload_to='main/images/', null=True, blank=True, max_length=100, verbose_name='Детальное фото 9')
    post_img10 = models.ImageField(upload_to='main/images/', null=True, blank=True, max_length=100, verbose_name='Детальное фото 10')
    video_1 = models.CharField('Видео 1', max_length=300, blank=True)
    video_2 = models.CharField('Видео 2', max_length=300, blank=True)
    video_3 = models.CharField('Видео 3', max_length=300, blank=True)
    video_4 = models.CharField('Видео 4', max_length=300, blank=True)
    class Meta:
        verbose_name_plural = 'Посты'
    
    def get_absolute_url(self):
        return reverse('detail',
                       args=[self.id,
                             self.slug])
    
    def __str__(self):
        return f'{self.title} - {self.tags.names()}'