#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.db import models


class Postt(models.Model):
    subject=models.CharField(max_length=100)
    content=models.TextField(max_length=500)
    select=models.BooleanField(blank=True)
   
    def __str__(self):
        return self.subject

class Post(models.Model):
    subject=models.CharField(max_length=100)
    content=models.TextField(max_length=500)
   
    def __str__(self):
        return self.subject

class Past(models.Model):
    your_name=models.CharField(max_length=100)
    your_age=models.TextField(max_length=500)
   
    def __str__(self):
        return self.your_name

