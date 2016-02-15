# -*- coding: utf-8 -*-
import django_filters
from django.db.models import Q
from models import Sadhu


class SubsFilter(django_filters.FilterSet):
    # переопределяем фильтр по умолчанию
    # теперь мы вместо точного значения названия, ищем совпадения по содержанию
    title = django_filters.CharFilter(name='username', lookup_type='icontains')

    class Meta:
        model = Sadhu
        fields = ['username', 'spiritual_name', 'last_name', 'first_name','middle_name']
