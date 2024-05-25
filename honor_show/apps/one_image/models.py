from django.db import models

class Field(models.Model):
    class Meta:
        verbose_name = 'رشته'
        verbose_name_plural = 'رشته ها'
    field_name = models.CharField(max_length=45, verbose_name='نام رشته', blank=False, null=False)
    

class Person(models.Model):
    class Meta:
        verbose_name = 'دارنده افتخار'
        verbose_name_plural = 'دارندگان افتخار'
        
    name = models.CharField(max_length=20, verbose_name='نام')
    family = models.CharField(max_length=20, verbose_name='نام خانوداگی')
    slug = models.SlugField()
    age = models.IntegerField(blank=True, null=False, verbose_name='سن')
    email = models.EmailField(max_length=100, blank=True, null=False, verbose_name='ایمیل')
    DEGREES = [
        ('under-diploma', 'زیر دیپلم'),
        ('diploma', 'دیپلم'),
        ('bachelor', 'کارشناسی'),
        ('master', 'کارشناسی ارشد'),
        ('Ph.d.', 'دکتری'),
    ]
    education_degree = models.CharField(choices=DEGREES, max_length=30, default='under-diploma', verbose_name='تحصیلات')
    education_field = models.ForeignKey(Field, on_delete=models.CASCADE, null=False, blank=False, verbose_name='رشته تحصیلی')
    
    
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
        ('other', 'المپیاد'),
    ]
    honor_field = models.CharField(choices=FIELDS, blank=False, max_length=20,  null=False, verbose_name = 'دسته افتخار')
    owner = models.ForeignKey(Person, on_delete=models.CASCADE, blank=False, null=False, verbose_name = 'دارنده عنوان')

    def __str__(self):
        return f'name: {self.name}, image_path: {self.image_path}'



    
    
    
