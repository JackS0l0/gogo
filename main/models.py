from django.db import models
from ckeditor.fields import RichTextField
class MainSettings(models.Model):
    mainText1=RichTextField('Текст на верху сайта на главном странице',default='none',null=True,blank=True)
    mainText2=RichTextField('Текст в конце сайта на главном странице',default='none',null=True,blank=True)
    logo=models.URLField('Логотип',default='',null=True,blank=True)
    logotxt=models.CharField('Текст в логотипе',max_length=200,default='',null=True,blank=True)
    footer=models.TextField('Текст в подвале',default='',null=True,blank=True)
    def __str__(self):
        return f'настойки'
    class Meta:
        verbose_name='Настройка'
        verbose_name_plural='Настройки'