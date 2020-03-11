from django.shortcuts import render
from .models import TblSeq
from django.http import HttpResponse


# Create your views here.

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        red = request.POST.get('red')
        blue = request.POST.get('blue')
        seq = TblSeq.objects.filter(red=red).all()
        ctx = {
            'red': red,
            'blue': blue,

        }
        ctx['seq'] = seq
        if seq:
            if seq[0].blue == blue:
                ctx['desc'] = '一等奖'
                return render(request, 'index.html', ctx)
            else:
                ctx['desc'] = '二等奖'
                return render(request, 'index.html', ctx)
        else:
            ctx['desc'] = '没中奖'
            return render(request, 'index.html', ctx)


'''
1、让03和输入3一样效果
2、用pyecharts绘制篮球的次数加上红球

'''
