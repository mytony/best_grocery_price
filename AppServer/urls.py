"""AppServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.contrib import admin
from best_price import views

urlpatterns = [
    url(r'^$', views.current_datetime, name='current_datetime'),
    url(r'^admin/', admin.site.urls),
    # ex: /product/Soap
    url(r'^product/(?P<name>[a-zA-Z]+)$', views.get_product),
    # ex: /products/10/5
    url(r'^products/(?P<page_size>[0-9]+)/(?P<page_num>[0-9]+)$', views.get_products),
    # ex: /product/create/<title>/<price>/<category>/<location>/
    url(r'^product/create/(?P<title>[0-9]+)/(?P<price>[0-9]+)/(?P<cat>[a-zA-Z]+)/(?P<loc>[0-9]+)$', views.create_product),
    # ex: /product/update/<id>/<title>/<price>/<category>/<location>/
    url(r'^product/update/(?P<id>[0-9]+)/(?P<title>[0-9]+)/(?P<price>[0-9]+)/(?P<cat>[a-zA-Z]+)/(?P<loc>[0-9]+)$', views.update_product),
    # ex: /products/search/<keyword>
    url(r'^products/search/(?P<keyword>[0-9]+)$', views.search_product),
]
