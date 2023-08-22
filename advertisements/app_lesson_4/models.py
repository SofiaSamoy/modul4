from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()
 
class Advertisement(models.Model):
    title = models.CharField(verbose_name='Название', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text= 'Укажите, если возможен торг')
    creat_at = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, verbose_name= 'Пользователь', on_delete= models.CASCADE)
    image = models.ImageField('Изображение', upload_to= 'advertisments/')
 
    @admin.display (description= 'Дата создания')
    def created_date(self):
        if self.creat_at.date() == timezone.now().date():
            created_time = self.creat_at.time().strftime('%H:%M:%S')
            return format_html('<span style = "color:green; font-weight:bold;"> Сегодня в {} </span>', created_time)
        return self.creat_at.strftime('%d.%m.%Y')
    
    @admin.display (description= 'Дата обновления')
    def updated_date(self):
        if self.update.date() == timezone.now().date():
            updated_time = self.update.time().strftime('%H:%M:%S')
            return format_html('<span style = "color:red; font-weight:bold;"> Сегодня в {} </span>', updated_time)
        return self.update.strftime('%d.%m.%Y')
    
    @admin.display (description= 'Изображения')
    def loaded_image(self):
        if self.image:
            return format_html('<img src="{url}" width="100" height="100" class="img-fluid rounded-start" alt="Card title">', url=self.image.url)
        
    def __str__(self):
        return f'Advertisement(id = {self.id}, title = {self.title}, price = {self.price})'
    
class Meta:
    db_table = 'advertisements'