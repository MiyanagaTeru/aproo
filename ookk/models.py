#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    subject=models.CharField(max_length=100)
    content=models.TextField(max_length=1000)
    def __str__(self):
        return self.subject

class Apost(models.Model):

    BBS_CHOICES=(

    ('RDHT','热点话题'),
	('TXDS','天下大势'),
	('SHZH','生活智慧'),
	('TTXS','天天向上'),
	('TGLJ','谈古论今'),
	('YLBG','娱乐八卦'),
	('JTGW','鸡汤感悟'),
	('JSXX','健身休闲'),
	('WSBB','无所不包'),
    )
    subject=models.CharField(max_length=100)
    content=models.TextField(max_length=1000)
    pimageA=models.ImageField(null=True,upload_to='pimageAs/%Y/%m/%d',height_field=None,width_field=None, max_length=100)
    pimageB=models.ImageField(null=True,upload_to='pimageBs/%Y/%m/%d',height_field=None,width_field=None, max_length=100)
    pimageC=models.ImageField(null=True,upload_to='pimageCs/%Y/%m/%d',height_field=None,width_field=None, max_length=100)
    pimageD=models.ImageField(null=True,upload_to='pimageDs/%Y/%m/%d',height_field=None,width_field=None, max_length=100)
    pimageE=models.ImageField(null=True,upload_to='pimageEs/%Y/%m/%d',height_field=None,width_field=None, max_length=100)
    select=models.BooleanField(default=False)
    bbs=models.CharField(max_length=4,choices=BBS_CHOICES,default='RDHT')
    pubdate=models.DateField(auto_now=True)
    counter=models.IntegerField(default=0)
    author=models.CharField(max_length=30,default='私人定制朋友圈/转')

    def __str__(self):
        return self.subject

class Apublisher(models.Model):
    user=models.OneToOneField(User,primary_key=True)
    advtext=models.TextField(blank=True,max_length=200)
    advimage=models.ImageField(null=True,upload_to='advimages/%Y/%m/%d',height_field=None,width_field=None, max_length=300)
    advimageA=models.ImageField(null=True,upload_to='advimageAs/%Y/%m/%d',height_field=None,width_field=None, max_length=300)
    advimageB=models.ImageField(null=True,upload_to='advimageBs/%Y/%m/%d',height_field=None,width_field=None, max_length=300)
    advimageC=models.ImageField(null=True,upload_to='advimageCs/%Y/%m/%d',height_field=None,width_field=None, max_length=300)
    advimageD=models.ImageField(null=True,upload_to='advimageDs/%Y/%m/%d',height_field=None,width_field=None, max_length=300)
    post=models.ManyToManyField(Apost,blank=True)
    advdate=models.DateField(auto_now=True)
    advcounter=models.IntegerField(default=0)


    def __str__(self):
        return self.user.username

    class Meta:
        ordering=('user',)
