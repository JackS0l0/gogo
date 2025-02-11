from django.shortcuts import render
from app.utils import common_data
from articles.models import Girls
def index(request):
    data = common_data()
    context={
        'title':'Interior Designer Portfolio',
        'girls':Girls.objects.all().order_by('-date')[0:16],
    }
    data.update(context)
    return render(request,'index.html',data)