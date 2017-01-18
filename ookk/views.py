#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from ook.forms import Pormset,Post,Pormsett,Postt
from ookk.forms import ApostForm,Apormset,UserRegisterForm,UploadForm,ApublisherForm
from ookk.models import Apost,Apublisher
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User,Permission
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse,resolve
from ookk import views as ookk_views
from django.contrib.auth.decorators import login_required
from datetime import datetime,timedelta
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
import re




def comein(request):
    '''u=request.user
    ua=request.user.is_authenticated()'''
    now=datetime.now()
    start7=now-timedelta(days=7)
    start30=now-timedelta(days=30)
    queryset=Apost.objects.filter(pubdate__gt=start7).order_by('-pubdate')[:30]
    topset=Apost.objects.filter(pubdate__gt=start30).order_by('-counter')[:30]
    return render(request,'comein.html',locals())
def comein_more1(request):
    '''u=request.user
    ua=request.user.is_authenticated()'''
    now=datetime.now()
    #start7=now-timedelta(days=7)
    start30=now-timedelta(days=30)
    queryset=Apost.objects.filter(pubdate__gt=start30).order_by('-pubdate')[30:70]
    #topset=Apost.objects.filter(pubdate__gt=start30).order_by('-counter')[:20]
    return render(request,'comein_more1.html',locals())
def comein_more2(request):
    '''u=request.user
    ua=request.user.is_authenticated()'''
    now=datetime.now()
    #start7=now-timedelta(days=7)
    start30=now-timedelta(days=30)
    #queryset=Apost.objects.filter(pubdate__gt=start30).order_by('-pubdate')[20:70]
    topset=Apost.objects.filter(pubdate__gt=start30).order_by('-counter')[30:70]
    return render(request,'comein_more2.html',locals())

def c_rdht(request):
    now=datetime.now()
    start30=now-timedelta(days=30)
    queryset=Apost.objects.filter(pubdate__gt=start30,bbs='RDHT').order_by('-pubdate')[:30]
    return render(request,'c_rdht.html',locals())

def c_txds(request):
    now=datetime.now()
    start30=now-timedelta(days=30)
    queryset=Apost.objects.filter(pubdate__gt=start30,bbs='TXDS').order_by('-pubdate')[:30]
    return render(request,'c_txds.html',locals())
def c_ylbg(request):
    now=datetime.now()
    start30=now-timedelta(days=30)
    queryset=Apost.objects.filter(pubdate__gt=start30,bbs='YLBG').order_by('-pubdate')[:30]
    return render(request,'c_ylbg.html',locals())

def c_shzh(request):
    now=datetime.now()
    start30=now-timedelta(days=30)
    queryset=Apost.objects.filter(pubdate__gt=start30,bbs='SHZH').order_by('-pubdate')[:30]
    return render(request,'c_shzh.html',locals())

def c_ttxs(request):
    now=datetime.now()
    start30=now-timedelta(days=30)
    queryset=Apost.objects.filter(pubdate__gt=start30,bbs='TTXS').order_by('-pubdate')[:30]
    return render(request,'c_ttxs.html',locals())
def c_tglj(request):
    now=datetime.now()
    start30=now-timedelta(days=30)
    queryset=Apost.objects.filter(pubdate__gt=start30,bbs='TGLJ').order_by('-pubdate')[:30]
    return render(request,'c_tglj.html',locals())
def c_jtgw(request):
    now=datetime.now()
    start30=now-timedelta(days=30)
    queryset=Apost.objects.filter(pubdate__gt=start30,bbs='JTGW').order_by('-pubdate')[:30]
    return render(request,'c_jtgw.html',locals())
def c_jsxx(request):
    now=datetime.now()
    start30=now-timedelta(days=30)
    queryset=Apost.objects.filter(pubdate__gt=start30,bbs='JSXX').order_by('-pubdate')[:30]
    return render(request,'c_jsxx.html',locals())
def search_feed(request):
    return render(request,'search_feed.html',locals())
def search(request):
    subj=request.GET.get('subject')
    if subj.strip()=='':return HttpResponse('请给点线索，搜索栏里不能为空')
    queryset=Apost.objects.filter(subject__icontains= subj.strip()).order_by('-pubdate')[:30]
    if not queryset:return HttpResponse('没有搜到符合条件的内容')
    return render(request,'search.html',locals())

def login_r(request):
    if request.method=='GET':
        l_pk=request.GET['pk']
    return render(request,'login_r_feed.html',locals())

def release_r(request):
  if request.method == 'GET':

    pkk=request.GET.get('pk')
    u= request.GET['username']

    pp=Apost.objects.get(pk=pkk)
    pp.counter=pp.counter+1
    pp.save()

    if not Apublisher.objects.filter(user__username=u):
      return HttpResponse('该用户须先完善个人资料，然后才能定制发布')
    pub=Apublisher.objects.get(user__username=u)
    if not pub.advimage :return HttpResponse('该用户展示内容不完备')
    pub.advcounter=pub.advcounter+1
    pub.save()
    return render(request,'release.html',locals())


def loginq(request):
    return render(request,'login_feed.html',locals())

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    if not re.match("^[a-zA-Z]\w+$",username) or not re.match("^\w+$",password) :
        return HttpResponse("用户名和密码只能用英文字母或数字，且用户名只能以英文字母开头")

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request,'login_view.html',locals())
    else:
        return HttpResponse('用户名或密码错误')

def login_up_view(request):
    username = request.POST['username']
    password = request.POST['password']
    if not re.match("^[a-zA-Z]\w+$",username) or not re.match("^\w+$",password) :
        return HttpResponse("用户名和密码只能用英文字母或数字，且用户名只能以英文字母开头")

    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return render(request,'uppublisher.html',locals())
    else:
        return HttpResponse('用户名或密码错误')

def logout_view(request):
    logout(request)
    return HttpResponse('你已经退出登录<a href="/loginq/"><input type="button" value="重新登录" action="loginq"></a>')


def register_feed(request):
    form=UserRegisterForm()
    return render(request,'register_feed.html',locals())

def userRegister(request):

        if request.method=='POST':
            form=UserRegisterForm(request.POST)
            if form.is_valid():
              username=form.cleaned_data['username']
              password=form.cleaned_data['password']
              password2=form.cleaned_data['password2']
              errors=[]
            if not re.match("^[a-zA-Z]\w+$",username) or not re.match("^\w+$",password) or not re.match("^\w+$",password2):
                return HttpResponse("用户名和密码只能用英文字母或数字，且用户名只能以英文字母开头")
            if password!=password2:
                errors.append("password not equall")
                return HttpResponse("两次输入的密码不一样")
            if len(password)<6 or len(username)<6:
                return HttpResponse('用户名和密码的长度不能小于6个英文字母或数字')
            if len(password)>20 or len(username)>20:
                return HttpResponse('用户名和密码的长度不能大于20个英文字母或数字')
            filterResult=User.objects.filter(username=username)
            if len(filterResult)>0:
                errors.append("name used")
                return HttpResponse('此用户名已被占用')
            user=User()
            user.username=username
            user.set_password(password)
            user.is_staff=True
            user.is_active
            user.save()
            user=get_object_or_404(User,username=username)
            perm=Permission.objects.get(codename='add_apost')
            user.user_permissions.add(perm)
            newUser=authenticate(username=username,password=password)
            if newUser is not None:
                login(request, newUser)
                return render(request,"userregister.html",locals())

def upup(request):
    form=UploadForm()
    return render(request,'upup.html',locals())


def looklook(request):
    if request.method == 'POST':
      if request.POST['subject']=='' or request.POST['content']=='':
        return HttpResponse('表单各项不能为空')
      if not 'pimageA' in request.FILES:
        return HttpResponse('请选择您要上传的图片')
      form = UploadForm(request.POST,request.FILES)
      if form.is_valid() and request.user.is_authenticated():       #
        sub=form.cleaned_data['subject']
        con=form.cleaned_data['content']
        ff=Apost(subject=sub,content=con,pimageA=request.FILES['pimageA'])
        ff.save()
        ff=Apost.objects.filter(subject=sub,content=con)


        return render(request,'lookimage.html',locals())



def req_user(request):
    if request.user.is_authenticated():
        req=request.user
        rr=request.user.pk
        uu=request.user.username
        uuuu=User.objects.get(username=uu)
        ap=Apublisher.objects.create(user=uuuu)
        ap.save()
    return render(request,'req_user.html',locals())


def uppublisher(request):
    if not request.user.is_authenticated():
        return render(request,'login_up.html',locals())
    if request.user.is_authenticated():
        return render(request,'uppublisher.html',locals())
def lookpubjpg(request):
    if request.user.is_authenticated():
       qname=request.user.username
       uuser=User.objects.get(username=qname)
    if not Apublisher.objects.filter(user=uuser):
         ap=Apublisher.objects.create(user=uuser)
         ap.save()
         if request.method == 'POST':
           form = ApublisherForm(request.POST,request.FILES)
           if form.is_valid():
             ap.advtext=request.POST['advtext']
             ap.advimage=request.FILES['advimage']
             ap.save()
             return render(request,'lookpubjpg.html',locals())
    if Apublisher.objects.filter(user=uuser):
         ap=Apublisher.objects.get(user=uuser)
         ap.save()
         if request.method == 'POST':
           form = ApublisherForm(request.POST,request.FILES)
           if not form.is_valid():
               return HttpResponse('请选择要上传的图片')
           if form.is_valid():
             ap.advimage=request.FILES['advimage']
             ap.advtext=request.POST['advtext']
             ap.save()
             return render(request,'lookpubjpg.html',locals())
    else:
        form=ApublisherForm()
        return render(request,'showform.html',locals())

def uploadonly(request):
    form=ApostForm()
    return render(request,'uploadonly.html',locals())
def lookonly(request):
    if request.method == 'POST':
      form = ApostForm(request.POST,request.FILES)
      if form.is_valid():
        pimageA=request.FILES['pimageA']
        if not pimageA.name.lower().endswith( (".jpg",".png",".gif",".tiff",".jpeg",".bmp",".tif")):
            return HttpResponse("图片格式只接受以下几种：jpg,jpeg,png,gif,tiff,tif,bmp")
        if pimageA.size>300000:
            return HttpResponse('图片文件不能超过250K')
        subject=request.POST['subject']
        content=request.POST['content']
        #if len(subject)>99 or len(content)>999:
        #    return HttpResponse('标题字数超限额')
        form.save()
        ff=Apost.objects.filter(subject=request.POST['subject'],content=request.POST['content'])
        return render(request,'lookonly.html',locals())


    else:
        form=ApostForm()
        return render(request,'showform.html',locals())


def upload(request):
    form=ApostForm()
    return render(request,'upload.html',locals())

def lookimage(request):
    if request.method == 'POST':
      form = ApostForm(request.POST,request.FILES)
      if form.is_valid():
        pimageA=request.FILES['pimageA']
        if not pimageA.name.lower().endswith( (".jpg",".png",".gif",".tiff",".jpeg",".bmp",".tif")):
            return HttpResponse("图片格式只接受以下几种：jpg,jpeg,png,gif,tiff,tif,bmp")
        if pimageA.size>300000:
            return HttpResponse('图片文件不能超过250K')

        form.save()
        ff=Apost.objects.filter(subject=request.POST['subject'],content=request.POST['content'])
        return render(request,'lookimage.html',locals())


    else:
        form=ApostForm()
        return render(request,'showform.html',locals())


def release(request):
    if request.method=='GET':
      pkk=request.GET.get('pk')
      pp=Apost.objects.get(pk=pkk)
      pp.counter=pp.counter+1
      pp.save()

      if request.user.is_authenticated():
         if not Apublisher.objects.filter(user=request.user):
             return HttpResponse('请先上传资料，完善用户展示内容')
         pub=Apublisher.objects.get(user=request.user)
         pub.advcounter=pub.advcounter+1
         pub.save()
      return render(request,'release.html',locals())


def readcontent(request):
    if request.method=='GET':
       pkk=request.GET.get('pkk')
       aff=Apost.objects.get(pk=pkk)
       aff.counter=aff.counter+1
       aff.save()
       return render(request,'readcontent.html',locals())

def guide(request):
    return render(request,'guide.html',locals())
