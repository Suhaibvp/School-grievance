"""student URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
# from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('studadd',views.studadd),
    path('sstudent',views.sstudent),
    path('ulogin',views.ulogin),
    path('logout',views.ulogout),
    path('prinsadd',views.prinsadd),
    path('sprince',views.sprince),
    path('hoadd',views.hoadd),
    path('shod',views.shod),
    path('creg',views.creg),
    path('cshow',views.cshow),
    path('cpshow',views.cpshow),
    path('chshow',views.chshow),
    path('rp/<int:id>',views.rp,name="rp"),
    path('rp/rrp/<int:id>',views.rrp,name="rrp"),
    path('rh/<int:id>',views.rh,name="rh"),
    path('rh/rrh/<int:id>',views.rrh,name="rrh"),
    path('csshow',views.csshow),
    path('cdelete/<int:id>',views.cdelete,name="cdelete"),
    path('pprofile',views.pprofile),
    path('hprofile',views.hprofile),
    path('sprofile',views.sprofile),
    path('studup/<int:id>',views.studup,name="studup"),

    


    # path('reg',views.reg),
    
    
    
    
    
    
    # path('sfview',views.sfview),
    
    # path('ufview',views.ufview),
    
    
    # path('vprofile',views.vprofile),
    # path('sdelete/<int:id>',views.sdelete,name="sdelete"),
    # path('supdate/<int:id>',views.supdate,name="supdate"),
    # path('supdate/ssupdate/<int:id>',views.ssupdate,name="ssupdate"),
    # path('uupdate/<int:id>',views.uupdate,name="uupdate"),
    # path('uupdate/uuupdate/<int:id>',views.uuupdate,name="uuupdate"),
    # path('udelete/<int:id>',views.udelete,name="udelete")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
