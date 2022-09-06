from django.db import models

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_ad = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_ad = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank = True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')#защита от удаления связанных данных

    def __str__(self): #чтобы не отображалось News.object..
        return self.title

    class Meta:
        #наименование модели в единственном числе
        verbose_name = 'Новость'
        # наименование модели во множественном числе
        verbose_name_plural = 'Новости'
        #как сортировать модели
        ordering = ['-created_ad']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index = True, verbose_name='Наименование категории')
    #индексирует данное поле, делает более удобным для поиска, verbose_name - как будет называться модель в админке

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ['title'] #сортировка по наименованию

# Create your models here.
