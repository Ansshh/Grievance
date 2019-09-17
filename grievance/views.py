from django.shortcuts import render,redirect
from .models import*
# Create your views here.

def home(request):

    list=['ram','anshit',1,2,3,5]
    dict={'garbage':0.50,'pothole':0.15,'sewage':0.25,'sanitation':0.10}
    return render(request,'index.html',dict)

def upload(request):
    if request.method=='POST':
        data=request.POST
        typ=data['type']
        rep=data['reporter']
        dep=data['dept']
        print(typ,rep,dep)
        obj=problems(ptype=typ,reporter=rep,department=dep)
        obj.save()
    return redirect('/')