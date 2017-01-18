#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from ook.models import Post,Past,Postt
from django.forms.models import modelformset_factory
from ookk.models import Apost,Book,Apublisher

class UserRegisterForm(forms.Form):
    username=forms.CharField(label='用户名',max_length=50)
    password=forms.CharField(label='密码',max_length=50,widget=forms.PasswordInput)
    password2=forms.CharField(label='密码确认',max_length=50,widget=forms.PasswordInput)

class UploadForm(forms.Form):
    subject=forms.CharField(label='标题',max_length=100)
    content=forms.CharField(label='正文',max_length=1000)
    pimageA=forms.ImageField(required=False,max_length=50)

class ApostForm(ModelForm):
   
   class Meta:
        model=Apost
        fields=['subject','content','bbs','pimageA']

class ApublisherForm(ModelForm):
   
   class Meta:
        model=Apublisher
        fields=['advimage']


Apormset=modelformset_factory(Apost,fields=('subject','content'),max_num=2)
