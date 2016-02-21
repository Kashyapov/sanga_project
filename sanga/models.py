# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core import validators
from django.core.mail import send_mail
from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from sanga_project import settings


class SignMonk(models.Model):
    name = models.CharField(_('Sign monk'), max_length=50)

    class Meta:
        verbose_name_plural = _('Sign monk')

    def __unicode__(self):
        return self.name


class StatusVidyaSadhana(models.Model):
    name = models.CharField(_('Status vidya sadhana'), max_length=50)

    class Meta:
        verbose_name_plural = _('Status vidya sadhana')

    def __unicode__(self):
        return self.name


class StatusBhakti(models.Model):
    name = models.CharField(_('Status bhakti'), max_length=100)

    class Meta:
        verbose_name_plural = _('Status bhakti')

    def __unicode__(self):
        return self.name


class StatusDonate(models.Model):
    name = models.CharField(_('Status donate'), max_length=100)

    class Meta:
        verbose_name_plural = _('Status donate')

    def __unicode__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(_('Level'), max_length=50)

    class Meta:
        verbose_name_plural = _('Level')

    def __unicode__(self):
        return self.name


class Citizenship(models.Model):
    name = models.CharField(_('Citizenship'), max_length=50)

    class Meta:
        verbose_name_plural = _('Citizenship')

    def __unicode__(self):
        return self.name


class AdditionalCharacteristic(models.Model):
    name = models.CharField(_('Additional characteristic'), max_length=100, default='', null=False, blank=False)

    class Meta:
        verbose_name_plural = _('Additional characteristic')

    def __unicode__(self):
        return self.name


class Town(models.Model):
    name = models.CharField(_('Town'), max_length=50)

    class Meta:
        verbose_name_plural = _('Towns')

    def __unicode__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(_('Country'), max_length=50)

    class Meta:
        verbose_name_plural = _('Countrys')

    def __unicode__(self):
        return self.name


class RatingSadhu(models.Model):
    """
    Таблица для учета заслуг (рейтинга) практикующих
    rating_from - кто оценивает
    rating_to - кого оценивают
    """
    rating_from = models.ForeignKey('Sadhu', verbose_name=_('rating from'), related_name='rating_from')
    rating_to = models.ForeignKey('Sadhu', related_name='rating_to')
    comment = models.CharField(_('Comment'), max_length=50, blank=True, default='')
    rating = models.IntegerField(_('Rating'))

    class Meta:
        verbose_name_plural = _('Rating')

    def __unicode__(self):
        return u'%s  %s  %s' % (self.rating_from, self.name, self.rating)


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError('User must have email')
        if not username:
            raise ValueError('User must have username')
        user = self.model(username=username, email=self.normalize_email(email))
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(username=username, email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


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
    spiritual_name = models.CharField(_('spiritual_name'), max_length=50, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    middle_name = models.CharField(_('middle_name'), max_length=30, blank=True)
    email = models.EmailField(_('email address'), blank=True)

    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        return "/users/%s/" % self.id

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

    def __unicode__(self):
        return self.username


class SadhuAdditional(models.Model):
    sadhu = models.OneToOneField(Sadhu)
    sign_monk = models.ForeignKey(SignMonk, verbose_name=_('Sign monk'), blank=True, null=True, on_delete=models.PROTECT)
    image = models.ImageField(_('Photo'), upload_to='images', blank=True)
    country = models.ForeignKey(Country, verbose_name=_('Country'),blank=True, null=True, on_delete=models.PROTECT)
    town = models.ForeignKey(Town, verbose_name=_('Town'), blank=True, null=True, on_delete=models.PROTECT)
    date_form = models.DateField(_('Date of filling in the questionnaire'), blank=True, null=True, default=timezone.now)
    phone = models.CharField(_('Phone'), max_length=30, blank=True, default='')
    soc_login = models.CharField(_('Skype, VK, Facebook'), max_length=100, blank=True, default='')
    status_vidya_sadhana = models.ForeignKey(StatusVidyaSadhana, verbose_name=_('Status vidya sadhana'), blank=True, null=True, on_delete=models.PROTECT)
    status_bhakti = models.ForeignKey(StatusBhakti, verbose_name=_('Status bhakti'), blank=True, null=True, on_delete=models.PROTECT)
    status_donate = models.ForeignKey(StatusDonate, verbose_name=('Status '), blank=True, null=True, on_delete=models.PROTECT)
    note = models.CharField(_('Note'), max_length=255, blank=True, default='')
    address = models.CharField(_('Address'), max_length=255, blank=True, default='')
    birthday = models.DateField(_('Birthday'), blank=True, null=True)
    level = models.ForeignKey(Level, verbose_name=_('Level'), blank=True, null=True, on_delete=models.PROTECT)
    symbol_of_faith = models.DateField(_('Symbol of faith'), blank=True, null=True)
    sharanam = models.DateField(_('Sharanam'), blank=True, null=True)
    place_of_birth = models.CharField(_('Place of Birth'), max_length=255, blank=True, default='')
    citizenship = models.ForeignKey(Citizenship, verbose_name=_('Citizenship'), blank=True, null=True, on_delete=models.PROTECT)
    education = models.CharField(_('Education'), max_length=255, blank=True, default='')
    max_add_rating = models.IntegerField(_('How can add rating'), default=1)
    additional_characteristic = models.ForeignKey(AdditionalCharacteristic, verbose_name=_('Additional characteristic'), blank=True, null=True, on_delete=models.PROTECT)

    def rating_sum(self):
        return RatingSadhu.objects.filter(rating_to = self.id).aggregate(Sum('rating'))

    class Meta:
        verbose_name = _('Sadhu additional')
        verbose_name_plural = _('Sadhus additional')

    def __unicode__(self):
        return self.sadhu.username





