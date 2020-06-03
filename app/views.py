from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.views.generic import View,TemplateView,DetailView,ListView
from .models import Person
from . import forms

# Create your views here.
def home(request):
    return render(request,"home.html")

class Nameslist(ListView):
    model=Person
    template_name="../templates/Person/person_list.html"

def detail(request):
    All_Names=Person.objects.values_list('name',flat=True)
    All_Credit=Person.objects.values_list('credit',flat=True)
    
    text={"obj":All_Names,
            "obj1":All_cred}
    return render(request,"details.html",text)

def add(request):    
    i=Person.objects.all().values()
    text={"obj":i}
    return render(request,"add.html",text)
def addc(request,id):
    try:
        det=Person.objects.all().values().filter(id=id)
        
        i=Person.objects.all().values()
        form=forms.formname()
        form.getform(id)
        print(form['Transfer_to'])

        text={"obj":det,
        "obj1":i,
        'form':form}
        for i in det:
            zz=i['credit']
        
        if request.method=='POST':
            f=forms.formname(request.POST)
            if f.is_valid():
                if int(f.cleaned_data['cred'])<=zz:

                    print(int(f.cleaned_data['cred']))
                    print(zz)
                    c=f.cleaned_data['cred']
                    d=f.cleaned_data['Transer_to']
                    print(d)
                    obj4=Person.objects.filter(id=id)
                    for k in obj4:
                        k.credit-=int(c)
                        k.save()
                    
                    obj3=Person.objects.filter(id=d)
                    for k in obj3:
                        k.credit+=int(c)
                        k.save()
                    return redirect("/home/list")
                else:
                    det=Person.objects.all().values().filter(id=id)
            
                    i=Person.objects.all().values()
                    form1=forms.formname()
                    form=form1.getform()
                    form["cred"].initial =f.cleaned_data['cred']
                    form["Transer_to"].initial =f.cleaned_data['Transer_to']
                    text="negative credits"
                    
                    text={"obj":det,
                    "obj1":i,
                    'form':form,
                    'err':text}
                    
                    return render(request,"cred.html",text)
            else:
                text={"obj":det,
                    "obj1":i,
                    'form':form,
                    'errMsg':"Enter some positive amount"}
                    
                return render(request,"cred.html",text)
                print(text)
        return render(request,"cred.html",text)
    except Exception as e:

        print('here')
        print(e)
    

def sucess(request,id):
    return HttpResponse("hello")