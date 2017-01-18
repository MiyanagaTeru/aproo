#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from ook.forms import PostForm,NameForm,PastForm
from ook.forms import Pormset,Post,Pormsett,Postt


def pormsett_feed(request):
    pormsett=Pormsett(queryset=Postt.objects.all())
    return render(request,'pormsett_feed.html',locals())
def pormsett_show(request):   
    if request.method == 'POST':               
      pormsett = Pormsett(request.POST)       
      if pormsett.is_valid():
          #pormsett.save
          for porm in pormsett:
              subject=porm.cleaned_data['subject']          
              content=porm.cleaned_data['content']
              select=porm.cleaned_data['select']
              p=Postt.objects.create(subject=subject,content=content,select=select)
              p.save()
      return render(request,'pormsett_show.html',locals())  
    else:
        pormsett=Pormsett()
        return render(request,'pormsett.html_show',locals())



def feedpormset(request):
    pormset=Pormset(queryset=Post.objects.all())
    return render(request,'feedpormset.html',locals())
def showpormset(request):   
    if request.method == 'POST':               
      pormset = Pormset(request.POST)       
      if pormset.is_valid():
          pormset.save
      # subject=form.cleaned_data['subject']          
      #content=form.cleaned_data['content']
      return render(request,'showpormset.html',locals())  
    else:
        pormset=Pormset()
        return render(request,'showpormset.html',locals())





def inputname(request):
    form=PastForm()
    return render(request,'inputname.html',locals())


def thank(request):
    return render(request,'thank.html')

def readgetname(request):   
    if request.method == 'POST':               
      form = PastForm(request.POST)       
      if form.is_valid():          
        your_age=form.cleaned_data['your_age']          
        your_name=form.cleaned_data['your_name']
        return render(request,'name.html',locals())  
    else:
        form=PastForm()
        return render(request,'showform.html',locals())



def feedform(request):
     #form=PostForm()
     form=NameForm()
     return render(request,'feedform.html',locals())


def showform(request):
    if request.method == 'POST':        
        #form = PostForm(request.POST)
        form=NameForm(request.POST)	
        if form.is_valid():
           subject=form.cleaned_data['subject']
           content=form.cleaned_data['content']
           #return HttpResponseRedirect('/showform/')
           return render(request,'showform.html',locals())
        else:
          form = PostForm()
          return render(request, 'showform.html', locals())



