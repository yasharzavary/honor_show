from django.db import models


class Honor(models.Model):
    class Meta:
        verbose_name = 'افتخار'
        verbose_name_plural = 'افتخارات'
        
    name = models.CharField(max_length=30, default='trhopy', verbose_name='عنوان')
    image_path = models.CharField(max_length=20, default='no_photo.jpg')
    desc = models.TextField(verbose_name='توضیحات', blank=True)
    when_get = models.DateTimeField(auto_now_add=True, blank=False, null=False, verbose_name='تاریخ کسب عنوان')
    slug = models.SlugField()
    FIELDS = [
        ('university', 'دانشگاهی'),
        ('compition', 'مسابقات'),
        ('olympi', 'المپیاد'),
    ]
    honor_field = models.CharField(choices=FIELDS, blank=False, max_length=20,  null=False, verbose_name='زمینه افتخار')

    def __str__(self):
        return f'name: {self.name}, image_path: {self.image_path}'


class Person(models.Model):
    class Meta:
        verbose_name = 'دارنده افتخار'
        verbose_name_plural = 'دارندگان افتخار'
    name = models.CharField(max_length=20, verbose_name='نام')
