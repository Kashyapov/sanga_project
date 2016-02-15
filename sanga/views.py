# -*- coding: utf-8 -*-
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from django.views.generic import ListView, DetailView, View
from django.views.generic.detail import SingleObjectMixin
from rest_framework import generics
from sanga.filters import SubsFilter
from sanga.models import Sadhu
from sanga.serializers import SubsSerializer


def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
        else:
            pass
    return render_to_response('accounts/login.html', context_instance=RequestContext(request))

def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')

class List(ListView):
    template_name = 'list.html'

    queryset = Sadhu.objects.all()

class ListDetail(DetailView):

    template_name = 'sadhu_detail.html'
    # queryset = Sadhu.objects.filter(is_active=True)

    model = Sadhu


class SubsView(generics.ListAPIView):
    queryset = Sadhu.objects.all()
    serializer_class = SubsSerializer
    filter_class = SubsFilter
    pagination_class = None