from django.shortcuts import render
from django.http import HttpResponse

from test1 import settings
from testbook.models import HeroInfo, BookInfo


# /
def index(request):
    return render(request,'testbook/index.html')


# /uppic
def uppic(request):
    return render(request, 'testbook/uppic.html')


# /ccpic
def ccpic(request):
    sm = request.POST.get('sm')
    sj = request.POST.get('sj')
    bread = request.POST.get('bread')
    bcomment = request.POST.get('bcomment')
    pic = request.FILES.get('pic')
    pic_url = '%s/testbook/%s' % (settings.MEDIR_ROOL, pic.name)
    with open(pic_url, 'wb') as file:
        for mes in pic.chunks():
            file.write(mes)
    BookInfo.objects.create(
        btitle=sm,
        bpub_date=sj,
        bread=bread,
        bcomment=bcomment,
        bimg='testbook/%s' % pic.name
    )
    return HttpResponse('恭喜你上传成功')
def select(request):
    b=BookInfo.objects.all()
    return render(request,'testbook/select.html',{'b':b})


