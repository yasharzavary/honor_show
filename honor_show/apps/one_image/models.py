from django.db import models




class honor(models.Model):
    class Meta:
        verbose_name = 'افتخار'
        verbose_name_plural = 'افتخارات'
        
    name = models.CharField(max_length=30, default='trhopy', verbose_name='نام')
    image_path = models.CharField(max_length=20, default='no_photo.jpg')
    desc = models.TextField(verbose_name='توضیحات', blank=True)
    when_get = models.DateTimeField(auto_now_add=True, blank=False, null=False, verbose_name='تاریخ کسب عنوان')
    
    def __str__(self):
        return f'name: {self.name}, image_path: {self.image_path}'
