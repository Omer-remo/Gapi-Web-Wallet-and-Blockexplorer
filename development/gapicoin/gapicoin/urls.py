#-*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
import gapicoin.views, gapicoin.apilist

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', gapicoin.views.landing),
    url(r'^login', gapicoin.views.login),
    url(r'^logout', gapicoin.views.logout),
    url(r'^transactions', gapicoin.views.ws),


    #REST API
    url(r'^api/v1/checkwallet/', gapicoin.views.checkwallet),
    url(r'^api/v1/sendgapicoin', gapicoin.views.sendgapicoin),
    url(r'^api/v1/createnewwallet/', gapicoin.views.createnewwallet),
    url(r'^api/v1/alltransactions/', gapicoin.apilist.alltransactions),
    url(r'^api/v1/gettransaction/(?P<tid>\w+)/$', gapicoin.apilist.gettransaction,  name='gettransaction'),
    url(r'^api/v1/getwalletfrompkey/(?P<pkey>\w+)/$', gapicoin.apilist.getwalletfrompkey, name='getwalletfrompkey'),
    url(r'^api/v1/getpublickeyfromprikey/(?P<private_key>\w+)/$', gapicoin.apilist.getpublickeyfromprikey, name='getpublickeyfromprikey'),
    url(r'^api/v1/getbalancefromwallet/(?P<wallet>\w+)/$', gapicoin.apilist.getbalancefromwallet, name='getbalancefromwallet'),
    url(r'^api/v1/getwalletdetails/(?P<wallet>\w+)/$', gapicoin.apilist.getwalletdetails, name='getwalletdetails'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
