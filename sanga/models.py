# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser, User
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Sum
from django.utils.timezone import now

class PriznakMonk(models.Model):
    name = models.CharField('Сангха', max_length=30)

    class Meta:
        verbose_name_plural = 'Сангха'

    def __unicode__(self):
            return self.name

class StatusVidyaSadhahy(models.Model):
    name = models.CharField('Статус видья-садханы', max_length=30)

    class Meta:
        verbose_name_plural = 'Статус видья-садханы'

    def __unicode__(self):
            return self.name

class StatusVSlugenii(models.Model):
    name = models.CharField('Статус в служении', max_length=30)

    class Meta:
        verbose_name_plural = 'Статус в служении'

    def __unicode__(self):
            return self.name

class StatusGertvovatilya(models.Model):
    name = models.CharField('Статус жертвователя', max_length=30)

    class Meta:
        verbose_name_plural = 'Статус жертвователя'

    def __unicode__(self):
            return self.name

class Stupen(models.Model):
    name = models.CharField('Ступень', max_length=30)

    class Meta:
        verbose_name_plural = 'Ступень'

    def __unicode__(self):
            return self.name

class Gragdanstvo(models.Model):
    name = models.CharField('Гражданство', max_length=30)

    class Meta:
        verbose_name_plural = 'Гражданство'

    def __unicode__(self):
            return self.name

class Samaya(models.Model):
    name = models.CharField('Самайя', max_length=30)

    class Meta:
        verbose_name_plural = 'Самайя'

    def __unicode__(self):
            return self.name

class Town(models.Model):
    name = models.CharField('Город', max_length=50)

    class Meta:
        verbose_name_plural = 'Город'

    def __unicode__(self):
            return self.name

class Country(models.Model):
    name = models.CharField('Страна', max_length=50)

    class Meta:
        verbose_name_plural = 'Страна'

    def __unicode__(self):
            return self.name

class RatingSadhu(models.Model):
    rating_from = models.ForeignKey('Sadhu', verbose_name='Рейтинг от', related_name='rating_from')
    rating_to = models.ForeignKey('Sadhu', related_name='rating_to')
    name = models.CharField('Комментарий', max_length=50, blank=True, default='')
    rating = models.IntegerField('Заслуги')

    class Meta:
        verbose_name_plural = 'Заслуги'

    def __unicode__(self):
            return u'%s  %s  %s' % (self.rating_from, self.name, self.rating)

class Sadhu(AbstractUser):
    samaya = models.ForeignKey(Samaya, verbose_name='Самайя', blank=True, null=True, on_delete=models.SET_NULL)
    priznak_monk = models.ForeignKey(PriznakMonk, verbose_name='Сангха', blank=True, null=True, on_delete=models.SET_NULL)
    spiritual_name = models.CharField('Духовное имя', max_length=50, blank=True, default='')
    middle_name = models.CharField('Отчество', max_length=50, blank=True, default='')
    image = models.ImageField('Фото', upload_to='images', blank=True)
    country = models.ForeignKey(Country, verbose_name='Страна', blank=True, null=True, on_delete=models.SET_NULL)
    town = models.ForeignKey(Town, verbose_name='Город', blank=True, null=True, on_delete=models.SET_NULL)
    date_ankety = models.DateField('Дата заполнения анкеты', blank=True, default=now)
    phone = models.CharField('Телефон', max_length=30, blank=True, default='')
    soc_login = models.CharField('Скайп, ВК, Фейсбук', max_length=100, blank=True, default='')
    status_vidya = models.ForeignKey(StatusVidyaSadhahy, verbose_name='Статус видья-садханы', blank=True, null=True, on_delete=models.SET_NULL)
    status_v_slugenii = models.ForeignKey(StatusVSlugenii, verbose_name='Статус в служении', blank=True, null=True, on_delete=models.SET_NULL)
    status_gertvovatilya = models.ForeignKey(StatusGertvovatilya, verbose_name='Статус жертвователя', blank=True, null=True, on_delete=models.SET_NULL)
    primechanie = models.CharField('примечание', max_length=255, blank=True, default='')
    address = models.CharField('Адрес', max_length=255, blank=True, default='')
    den_rogdeniya = models.DateField('День рождения', null=True, blank=True )
    stupen = models.ForeignKey(Stupen, verbose_name='Ступень', blank=True, null=True, on_delete=models.SET_NULL)
    simvol_very = models.DateField('Сим Веры', blank=True, null=True)
    pribegishe = models.DateField('Прибежище', blank=True, null=True)
    mesto_rogdeniya = models.CharField('Место рождения', max_length=255, blank=True, default='')
    gragdanstvo = models.ForeignKey(Gragdanstvo, verbose_name='Гражданство', blank=True, null=True, on_delete=models.SET_NULL)
    obrazovanie = models.CharField('Образование', max_length=255, blank=True, default='')
    max_add_rating = models.IntegerField('Сколько может добавить заслуг', default=1)

    def rating_sum(self):
        return RatingSadhu.objects.filter(rating_to = self.id).aggregate(Sum('rating'))

    class Meta:
        verbose_name_plural = 'Садху'

    def get_absolute_url(self):
        return 'list/' + str(self.pk)

    def __unicode__(self):
        return self.username

