# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-27 12:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=1000)),
                ('pimageA', models.ImageField(null=True, upload_to='pimageAs/%Y/%m/%d')),
                ('pimageB', models.ImageField(null=True, upload_to='pimageBs/%Y/%m/%d')),
                ('pimageC', models.ImageField(null=True, upload_to='pimageCs/%Y/%m/%d')),
                ('pimageD', models.ImageField(null=True, upload_to='pimageDs/%Y/%m/%d')),
                ('pimageE', models.ImageField(null=True, upload_to='pimageEs/%Y/%m/%d')),
                ('select', models.BooleanField(default=False)),
                ('bbs', models.CharField(choices=[('RDHT', '热点话题'), ('TXDS', '天下大势'), ('SHZH', '生活智慧'), ('TTXS', '天天向上'), ('TGLJ', '谈古论今'), ('YLBG', '娱乐八卦'), ('JTGW', '鸡汤感悟'), ('JSXX', '健身休闲'), ('WSBB', '无所不包')], default='RDHT', max_length=4)),
                ('pubdate', models.DateField(auto_now=True)),
                ('counter', models.IntegerField(default=0)),
                ('author', models.CharField(default='私人定制朋友圈/转', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Apublisher',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('advtext', models.TextField(blank=True, max_length=200)),
                ('advimage', models.ImageField(max_length=300, null=True, upload_to='advimages/%Y/%m/%d')),
                ('advimageA', models.ImageField(max_length=300, null=True, upload_to='advimageAs/%Y/%m/%d')),
                ('advimageB', models.ImageField(max_length=300, null=True, upload_to='advimageBs/%Y/%m/%d')),
                ('advimageC', models.ImageField(max_length=300, null=True, upload_to='advimageCs/%Y/%m/%d')),
                ('advimageD', models.ImageField(max_length=300, null=True, upload_to='advimageDs/%Y/%m/%d')),
                ('advdate', models.DateField(auto_now=True)),
                ('advcounter', models.IntegerField(default=0)),
                ('post', models.ManyToManyField(blank=True, to='ookk.Apost')),
            ],
            options={
                'ordering': ('user',),
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('content', models.TextField(max_length=1000)),
            ],
        ),
    ]
