# from django.core.validators import RegexValidator
# -*- coding: utf-8 -*-
#Авторизація взята звідси http://www.yablochkin.net/django-simplereg/
#from sorl.thumbnail import ImageField
import datetime
from django.db import models
from sorl.thumbnail.shortcuts import get_thumbnail
from django.db.models.signals import post_save
#from django.dispatch import receiver
#from PIL import Image
#from io import StringIO
from django.contrib.auth.models import User


User.__unicode__ = lambda x: x.email



class Rating(models.Model):
    rate_name = models.CharField(max_length=15, blank=True)

    def __unicode__(self):
        return self.rate_name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    APPEAR_CHOICE = (
        ('1', 'Доступна'),
        ('0', 'Недоступна'),
    )
    # phoneRegexp = '/^((((\(\d{3}\))|(\d{3}-))\d{3}-\d{4})|(\+?\d{1,3}((-| |\.)(\(\d{1,4}\)(-| |\.|^)?)?\d{1,8}){1,5}))(( )?(x|ext)\d{1,5}){0,1}$/'
    fb_acc = models.BigIntegerField(max_length=255, blank=True, null=True)
    gplus_acc = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    #email = models.EmailField(blank=True)
    #password = models.CharField(max_length=50, )
    #group = models.ManyToManyField(Groups, verbose_name='Група')
    #permission = models.ManyToManyField(Permissions, verbose_name='Дозволи')
 #   avatar = models.ImageField(upload_to='Avatars',
 #                              name='%s_%s_%s' % ('id', 'first_name', 'last_name'),
 #                              verbose_name='Виберіть аватарку',
 #                              blank=True)  # треба буде дописати функцію для генерації шляху збереження
    contact_appear = models.CharField(max_length=1, choices=APPEAR_CHOICE, default='1')
    #profile_created = models.DateTimeField(auto_now_add=True)
    rate_id = models.ForeignKey(Rating, default='1')

    def __str__(self):
        return self.user.email



def create_user_profile(sender, instance, created, **kwargs):
    if created:
       profile, created = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User)


class Categories(models.Model):
    cat_name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.cat_name


class Tovar(models.Model):
    name = models.CharField(max_length=60, verbose_name='Назва товару')
    description = models.TextField(verbose_name='Опис')
    user = models.ForeignKey(User, verbose_name='Виберіть користувача')
    category_id = models.ManyToManyField(Categories, verbose_name='Виберіть категорію')
    archive = models.BooleanField(default=None, blank=True, verbose_name='Додати в архів')
    cache_array = models.TextField(default='cache')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name='Ціна')
    price_null = models.BooleanField(default=None, blank=True, verbose_name='Безкоштовно')
    price_description = models.CharField(max_length=255, blank=True, verbose_name='Коментарі до ціни')
    delivery = models.CharField(default='Самовивоз', max_length=128, verbose_name='Доставка')
    date_archive = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Додано до архіву')

    def __unicode__(self):
        return u'%s' % self.name


def p_path(self, filename):
        path_file = str(datetime.date.today())
        return u'%s/%s' % (path_file, filename.lower())


class Pictures(models.Model):
    tovar = models.ForeignKey(Tovar)
    pic_name = models.CharField(max_length=32, blank=True)  # треба прописати функцію для генерації імені
    p_path.short_description = u'prb'
    pic_path = models.ImageField(upload_to=p_path, blank=True)  # треба прописати функцію для генерації шляху

    def get_thumbnail_html(self):
        img = self.pic_path
        img_resize_url = unicode(get_thumbnail(img, '150x150').url)
        html = '<a class="image-picker" href="%s"><img src="%s" alt="%s"/></a>'
        return html % (self.pic_path.url, img_resize_url, self.pic_name)

    get_thumbnail_html.short_description = u'Мsниатюра'
    get_thumbnail_html.allow_tags = True

    def __unicode__(self):
        return u'%s' % self.pic_path


class Comments(models.Model):
    tovar = models.ForeignKey(Tovar)
    comments = models.TextField()
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)


class Bets(models.Model):
    user = models.ForeignKey(User)
    bet_date = models.DateTimeField(auto_now_add=True)
    tovar = models.ForeignKey(Tovar)

    class Meta:
        unique_together = (('user','tovar'),)

    def __unicode__(self):
        return u'%d' % self.tovar_id



# Create your models here.
