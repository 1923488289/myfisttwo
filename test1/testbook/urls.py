from django.conf.urls import url
from testbook import views

urlpatterns = [

    url(r'^$',views.index),#主页
    url(r'^uppic$',views.uppic),#上传图书信息
    url(r'^ccpic$',views.ccpic),#信息保存
    url(r'^select$',views.select),#查询书籍
    url(r'^heromess(\d+)$',views.heromess),#查询信息
    url(r'^upcreate$',views.upcreate),#上传信息
    url(r'^heromessage(\d+)$',views.heromessage),#保存信息
    url(r'^uphero$',views.uphero),# 继续上传人物信息
    # url(r'^heroxx(\d+)$',views.heroxx)

]
