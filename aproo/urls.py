"""aproo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from ook import views as ook_views
from ookk import views as ookk_views
from django.contrib.auth import views as auth_views

from django.conf.urls import url, include
from django.contrib.auth.models import User


urlpatterns = [
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', auth_views.login,{'template_name': 'login_feed.html'}),
    url(r'^upload/',ookk_views.upload),
    url(r'^lookimage/',ookk_views.lookimage),
    url(r'^register_feed/',ookk_views.register_feed),
    url(r'^logout_view/',ookk_views.logout_view),
    url(r'^login_view/',ookk_views.login_view),
    url(r'^login_up_view/',ookk_views.login_up_view),
    url(r'^release_r/',ookk_views.release_r),
    url(r'^loginq/',ookk_views.loginq),
    url(r'^login_r/',ookk_views.login_r),
    url(r'^upup/',ookk_views.upup,name='uupp'),
    url(r'^looklook/',ookk_views.looklook),
    url(r'^release/',ookk_views.release),
    url(r'^uppublisher/',ookk_views.uppublisher),
    url(r'^lookpubjpg/',ookk_views.lookpubjpg),
    url(r'^req_user/',ookk_views.req_user),
    url(r'^uploadonly/',ookk_views.uploadonly),
    url(r'^lookonly/',ookk_views.lookonly),
    url(r'^$',ookk_views.comein),
    url(r'^comein/',ookk_views.comein),
    url(r'^comein_more1',ookk_views.comein_more1),
    url(r'^comein_more2',ookk_views.comein_more2),
    url(r'^c_rdht/',ookk_views.c_rdht),
    url(r'^c_txds/',ookk_views.c_txds),
    url(r'^c_ylbg/',ookk_views.c_ylbg),
    url(r'^c_shzh/',ookk_views.c_shzh),
    url(r'^c_ttxs/',ookk_views.c_ttxs),
    url(r'^c_tglj/',ookk_views.c_tglj),
    url(r'^c_jtgw/',ookk_views.c_jtgw),
    url(r'^c_jsxx/',ookk_views.c_jsxx),
    url(r'^search_feed/',ookk_views.search_feed),
    url(r'^search/',ookk_views.search),
    url(r'^readcontent/',ookk_views.readcontent),
    url(r'^guide/',ookk_views.guide),
    url(r'^userRegister/',ookk_views.userRegister),
    #url(r'^display_lots/',ookk_views.display_lots),
    #url(r'^display_one/',ookk_views.display_one),
    #url(r'^pormsett_feed/',ookk_views.pormsett_feed),
    #url(r'^pormsett_show/',ookk_views.pormsett_show),
    #url(r'^', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
