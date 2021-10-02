from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import Register
from django.contrib.auth import authenticate,login
import mysql.connector
from json import dumps
from efarma import models

user_id=0
user_name=""

def home(request):
    mydb=mysql.connector.connect(host="localhost",user="root",password="windows10",database="farmaproduct",buffered=True)
    curr=mydb.cursor()
    currNext=mydb.cursor()
    sql="select * from efarma_products"
    curr.execute(sql)
    data={}
    count=0
    current_user=request.user
    global user_id
    user_id = current_user.id
    global user_name
    user_name = current_user.username
    for i in curr:
        v={'Name':i[6],'image':i[5],'company':i[2],'price':i[0],'category':i[1]}
        data.update({count:v})
        count+=1
    dataJson=dumps(data)

    sql = "select * from efarma_customer"
    mql="select id,username from auth_user"
    curr.execute(sql)
    currNext.execute(mql)
    diki={}
    for i in currNext:
        diki[i[0]]=i[1]

    col_of_review=curr.fetchall()
    count=0
    d = {}

    for i in col_of_review:
        v={'image':i[0],'name':diki[i[1]],'review':i[2]}
        d.update({count:v})
        count+=1
    dJson = dumps(d)

    sql = "select * from efarma_customer"
    curr.execute(sql)
    data1 = {}
    for i in curr:
        if user_id==i[1]:
         data1['image'] = i[0]
         data1['name'] = user_name
         data1['id']=user_id
         data1['review']=i[2]
         break
    dataJson1=dumps(data1)

    res=render(request, 'efarma/home.html',{'data':dataJson,'data1':dataJson1,'d':dJson})
    return res

def pesticide(request):
    mydb = mysql.connector.connect(host="localhost", user="root", password="windows10", database="farmaproduct")
    curr = mydb.cursor()
    sql = "select * from efarma_products"
    curr.execute(sql)
    data = {}
    count = 0
    for i in curr:
        if i[1]=='Pesticide':
          v = {'Name': i[6], 'image': i[5], 'company': i[2], 'price': i[0], 'category': i[1]}
          data.update({count: v})
          count += 1
    dataJson = dumps(data)
    res = render(request, 'efarma/home.html', {'data': dataJson})
    curr.close()
    return res

def fertilizers(request):
    mydb = mysql.connector.connect(host="localhost", user="root", password="windows10", database="farmaproduct")
    curr = mydb.cursor()
    sql = "select * from efarma_products"
    curr.execute(sql)
    data = {}
    count = 0
    for i in curr:
        if i[1].find("fertilizer")!=-1:
            v = {'Name': i[6], 'image': i[5], 'company': i[2], 'price': i[0], 'category': i[1]}
            data.update({count: v})
            count += 1
    dataJson = dumps(data)
    res = render(request, 'efarma/home.html', {'data': dataJson})
    curr.close()
    return res

def insecticide(request):
    mydb = mysql.connector.connect(host="localhost", user="root", password="windows10", database="farmaproduct")
    curr = mydb.cursor()
    sql = "select * from efarma_products"
    curr.execute(sql)
    data = {}
    count = 0
    for i in curr:
        if i[1].find("Insecticide")!=-1:
            v = {'Name': i[6], 'image': i[5], 'company': i[2], 'price': i[0], 'category': i[1]}
            data.update({count: v})
            count += 1
    dataJson = dumps(data)
    res = render(request, 'efarma/home.html', {'data': dataJson})
    curr.close()
    return res

def customerOrder(request):
    return render(request, 'efarma/yourorder.html')

def userLogin(request):
    data={}
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect("http://localhost:8000/FarmaHome/")
        else:
            data['error']='Either username or password is incorrect'
            return render(request,"efarma/login.html",data)
    else:
        return render(request, 'efarma/login.html',data)

def register(request):
    if request.method == 'POST':
       form = Register(request.POST,request.FILES)
       if form.is_valid():
           Customer = models.Customer()
           Customer.customerImage = form.cleaned_data.get("Enter_your_image")
           Customer.link = form.save()
           Customer.save()
           return redirect("http://localhost:8000/FarmaHome/userlogin/")
    else:
        form=Register()
    return render(request, 'efarma/register.html', {"form": form})

@csrf_exempt
def review(request):
    mydb = mysql.connector.connect(host="localhost", user="root", password="windows10", database="farmaproduct")
    curr = mydb.cursor()
    sql = "select * from efarma_customer"
    curr.execute(sql)
    input = request.GET.get('userInput')
    curr.fetchall()
    curr.execute("update efarma_customer set review='{}' where link_id={}".format(input,user_id))
    mydb.commit()
    mydb.close()
    return render(request, 'efarma/home.html')

