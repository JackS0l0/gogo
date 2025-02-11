from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
class Locations(models.Model):
    name=models.CharField('Место',max_length=200,default='')
    slug=models.SlugField('Slug',default='')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Место'
        verbose_name_plural='Места'
class Girls(models.Model):
    name=models.CharField('Имя',max_length=200,default='')
    slug=models.SlugField('Slug',default='')
    loc=models.ForeignKey(to=Locations,verbose_name='Место',on_delete=models.CASCADE)
    img=models.URLField('Фото',default='')
    img2=models.URLField('Фото2',default='',null=True,blank=True)
    img3=models.URLField('Фото3',default='',null=True,blank=True)
    img4=models.URLField('Фото4',default='',null=True,blank=True)
    img5=models.URLField('Фото5',default='',null=True,blank=True)
    img6=models.URLField('Фото6',default='',null=True,blank=True)
    img7=models.URLField('Фото7',default='',null=True,blank=True)
    img8=models.URLField('Фото8',default='',null=True,blank=True)
    img9=models.URLField('Фото9',default='',null=True,blank=True)
    img10=models.URLField('Фото10',default='',null=True,blank=True)
    num=models.CharField('Номер телефона',max_length=200,default='054-9140720')
    numlink=models.CharField('Линк на номер',max_length=200,default='+549140720')
    desc=RichTextField('Описание',default='none')
    date=models.DateTimeField('Дата',default=timezone.now)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Девушка'
        verbose_name_plural='Девушки'