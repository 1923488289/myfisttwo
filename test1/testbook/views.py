from django.shortcuts import render, redirect
from django.http import HttpResponse
from test1 import settings
from testbook.models import HeroInfo, BookInfo


# /
def index(request):
    return render(request, 'testbook/index.html')


# /uppic
def uppic(request):
    return render(request, 'testbook/uppic.html')


# /ccpic
def ccpic(request):
    sm = request.POST.get('sm')
    if not BookInfo.objects.filter(btitle=sm):

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
        # b=BookInfo.objects.filter(btitle=sm)
        return render(request, 'testbook/uphero.html')
    else:
        return redirect('/uppic')




# upcreate
def upcreate(request):
    hname = request.POST.get('hname')
    if not HeroInfo.objects.filter(hname=hname):
        hgender = request.POST.get('hgender')
        hcomment = request.POST.get('hcomment')
        hbook = request.POST.get('hbook')
        pic = request.FILES.get('pichero')
        pic_url = '%s/testhero/%s' % (settings.MEDIR_ROOL, pic.name)
        with open(pic_url, 'wb') as file:
            for file_1 in pic.chunks():
                file.write(file_1)
        if BookInfo.objects.filter(btitle=hbook):
            b = BookInfo.objects.get(btitle=hbook)
            # print(a)
            # b=BookInfo.objects.get(id=a.id)
            print(b)
            HeroInfo.objects.create(
                hname=hname,
                hgender=int(hgender),
                hcomment=hcomment,
                hbook=b,
                himg='testhero/%s' % pic.name
            )

            return render(request, 'testbook/reset.html')
        else:
            return render(request, 'testbook/err.html')
    else:
        return redirect('/uphero')

# /uphero
def uphero(request):
    # return redirect('/uphero')
    return render(request, 'testbook/uphero.html')


# /select
def select(request):
    b = BookInfo.objects.all()
    return render(request, 'testbook/select.html', {'b': b})

# heromess
def heromess(request, i):
    b = BookInfo.objects.get(id=int(i))
    heros = b.heroinfo_set.all()
    return render(request, 'testbook/selecthero.html', {'heros': heros})


# /heromessage
def heromessage(request, i):
    # b = BookInfo.objects.get(id=int(i))
    # heros = b.heroinfo_set.all()
    hero=HeroInfo.objects.get(id=int(i))
    print(hero.hname)
    return render(request, 'testbook/heros.html', {'hero':hero})



# /heroxx
# def heroxx(request,hero):
#     return HttpResponse(hero)
