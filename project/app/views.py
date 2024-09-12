from django.shortcuts import render

# Create your views here.

def set(request):
    list1={'id':1,'name':'surya','city':'bhopal'}
    list2={'id':2,'name':'ram','city':'indore'}
    list=[list1,list2]
    request.session['data']=list
    return render(request,'set.html')

def get(request):
    data1=request.session.get('data','guest')
    return render(request,'get.html',{'name':data1})


def delete(request):
    # data1=request.session.get('data','guest')
    # if 'data' in request.session:
    #     del request.session['name']
    request.session.flush()
    return render (request,'delete.html')
    