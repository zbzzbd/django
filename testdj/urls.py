"""testdj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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


    from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]
"""

from django.conf.urls import url
from testdj.view import hello
from learn.views import *
import people.views
from django.contrib import admin

admin.autodiscover()

urlpatterns =[url(r'^hello/',hello),
              url(r'^admin/', admin.site.urls),
              #url(r'^learn/',learn),
              url(r'^add/$',add,name='add'),
              url(r'^add/(\d+)/(\d+)/$',add2,name='add2'),
              url(r'^index/$',index,name='home'),
              url(r'^string',string,name='string'),
              url(r'^index1$',people.views.index1,name='home2')

              ]

