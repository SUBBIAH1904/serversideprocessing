from django.shortcuts import render
from datetime import datetime
# Create your views here.


def home(request):
    context={}
    context['Timestamp']=datetime.now().strftime("%d %m %y %H:%M:%S")
    return render(request,'myapp/home.html',context)
