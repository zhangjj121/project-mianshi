from django.shortcuts import render, redirect
from django.db import connection
# Create your views here.
from hr.models import AllMessage, Password, FangInfo


def login(request):
    if request.method=='GET':
        return render(request,'login.html')

    else:
        message = Password()
        user = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        if user and pwd:
            if Password.objects.get(user=user,password=pwd):
                request.session['user']=user
                return render(request,'shouye.html')
            else:
                return redirect('/hr/login/')



def fang_in(request):
    if request.method == 'GET':
        return render(request,'fang_in.html')
    else:
        new_fang = FangInfo()
        person =int(request.POST['put_person'])

        xq = request.POST['xiaoqu']

        lh = request.POST['louhao']

        dy = request.POST['danyuan']

        fj = request.POST['fjnumber']

        oldfang = FangInfo.objects.filter(xiaoqu=xq,
                                          louhao=int(lh),
                                          danyuan=int(dy),
                                          fjnumber=int(fj))
        if oldfang:
            return render(request,'fang_in.html',{'message':'房源已存在'})
        new_fang.put_person = AllMessage.objects.get(id=int(person))
        new_fang.xiaoqu = request.POST['xiaoqu']
        new_fang.louhao = request.POST['louhao']
        new_fang.danyuan = request.POST['danyuan']
        new_fang.chaoxiang = request.POST['chaoxiang']
        new_fang.fjnumber = request.POST['fjnumber']
        new_fang.mianji = request.POST['mianji']
        new_fang.price = request.POST['price']

        new_fang.save()
        return  redirect('/hr/fang_info/')


def fang_info(request):
    fang = FangInfo.objects.all().order_by('-id')
    return render(request,'fang_info.html',{'fang':fang})


def login_out(request):
    del request.session['user']
    return render(request,'login.html')



