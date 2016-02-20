# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core import validators
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, True, True,
                                 **extra_fields)


class Sadhu(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(
        _('username'),
        max_length=30,
        unique=True,
        help_text=_('Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[
            validators.RegexValidator(
                r'^[\w.@+-]+$',
                _('Enter a valid username. This value may contain only '
                  'letters, numbers ' 'and @/./+/-/_ characters.')
            ),
        ],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    spiritual_name = models.CharField(_('spiritual_name'), max_length=50, blank=True, default='')
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    middle_name = models.CharField(_('middle_name'), max_length=30, blank=True, default='')
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s %s' % (self.last_name, self.first_name, self.middle_name)
        return full_name.strip()

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])


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

class AdditionalCharacteristic(models.Model):
    name = models.CharField(_('Additional characteristic'), max_length=100, default='', null=False, blank=False)

    class Meta:
        verbose_name_plural = _('Additional characteristic')

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

# class SadhuAdditional(models.Model):
#     priznak_monk = models.ForeignKey(PriznakMonk, verbose_name='Сангха', blank=True, null=True, on_delete=models.SET_)
#
#     image = models.ImageField('Фото', upload_to='images', blank=True)
#     country = models.ForeignKey(Country, verbose_name='Страна', blank=True, null=True, on_delete=models.SET_NULL)
#     town = models.ForeignKey(Town, verbose_name='Город', blank=True, null=True, on_delete=models.SET_NULL)
#     date_ankety = models.DateField('Дата заполнения анкеты', blank=True, default=now)
#     phone = models.CharField('Телефон', max_length=30, blank=True, default='')
#     soc_login = models.CharField('Скайп, ВК, Фейсбук', max_length=100, blank=True, default='')
#     status_vidya = models.ForeignKey(StatusVidyaSadhahy, verbose_name='Статус видья-садханы', blank=True, null=True, on_delete=models.SET_NULL)
#     status_v_slugenii = models.ForeignKey(StatusVSlugenii, verbose_name='Статус в служении', blank=True, null=True, on_delete=models.SET_NULL)
#     status_gertvovatilya = models.ForeignKey(StatusGertvovatilya, verbose_name='Статус жертвователя', blank=True, null=True, on_delete=models.SET_NULL)
#     primechanie = models.CharField('примечание', max_length=255, blank=True, default='')
#     address = models.CharField('Адрес', max_length=255, blank=True, default='')
#     den_rogdeniya = models.DateField('День рождения', null=True, blank=True )
#     stupen = models.ForeignKey(Stupen, verbose_name='Ступень', blank=True, null=True, on_delete=models.SET_NULL)
#     simvol_very = models.DateField('Сим Веры', blank=True, null=True)
#     pribegishe = models.DateField('Прибежище', blank=True, null=True)
#     mesto_rogdeniya = models.CharField('Место рождения', max_length=255, blank=True, default='')
#     gragdanstvo = models.ForeignKey(Gragdanstvo, verbose_name='Гражданство', blank=True, null=True, on_delete=models.SET_NULL)
#     obrazovanie = models.CharField('Образование', max_length=255, blank=True, default='')
#     max_add_rating = models.IntegerField('Сколько может добавить заслуг', default=1)
#     additional_characteristic = models.ForeignKey(AdditionalCharacteristic, verbose_name=_('Additional characteristic'), blank=True, null=True, on_delete=models.PROTECT)
#
#     def rating_sum(self):
#         return RatingSadhu.objects.filter(rating_to = self.id).aggregate(Sum('rating'))
#
#     class Meta:
#         verbose_name_plural = 'Садху'
#
#     def get_absolute_url(self):
#         return 'list/' + str(self.pk)
#
#     def __unicode__(self):
#         return self.username
#
