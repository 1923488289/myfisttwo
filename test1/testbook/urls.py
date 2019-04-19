from django.conf.urls import url
from testbook import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^uppic$',views.uppic),
    url(r'^ccpic$',views.ccpic),
    url(r'^select$',views.select),

]
