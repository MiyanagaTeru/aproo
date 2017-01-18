#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django import forms
from django.forms import ModelForm
from ook.models import Post,Past,Postt
from django.forms.models import modelformset_factory

Pormset=modelformset_factory(Post,fields=('subject','content'),max_num=2)
Pormsett=modelformset_factory(Postt,fields=('subject','content','select'),max_num=2)

class PosttForm(ModelForm):
   class Meta:
        model=Postt
        fields=['subject','content','select']

class PastForm(ModelForm):
   class Meta:
        model=Past
        fields=['your_name','your_age']

class PostForm(ModelForm):
   class Meta:
        model=Post
        fields=['subject','content']

class NameForm(forms.Form):
    your_name=forms.CharField(label='yourname',max_length=100)
    your_age=forms.CharField(label='yourage',max_length=100)
