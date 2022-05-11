from django.shortcuts import HttpResponse,render
from CarRental.models import Contact
from CarRental.models import Car_Selection
from CarRental.models import Rental_History
from datetime import datetime
def index(request):
    #return HttpResponse("Hello, world. You're agfdgdfd polls index.")
     return render(request,'index.html')
def about(request):
     return render(request,'about.html')
def services(request):
    return render(request, 'service.html')
def help(request):
    return render(request, 'help.html')
def a(request):
     return render(request, 'a.html')
def b(request):
    return render(request, 'b.html')
def c(request):
    return render(request, 'c.html')
def howitworks(request):
    return render(request, 'howitworks.html',)
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get("phone")
        msg = request.POST.get('text')
        contact = Contact(name = name,email = email,phone = phone,msg = msg,date = datetime.today())
        contact.save()
    return render(request, 'contact.html',)


import mysql.connector as sql
fn =''
ln = ''
pwd = ''
mname = ''
mail = ''
mph = ''
mbill = ''
mcard = ''
mdriv= ''
madd = ''
date= ''
# Create your views here.
def login(request):
    global em, pwd
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="1234", database='CarRenting')
        cursor = m.cursor()
        d = request.POST
        if request.POST.get("checkbox") == "member":
            for key, value in d.items():
                if key == "email":
                    em = value
                if key == "password":
                    pwd = value
            c = "select * from member where MemberID='{}' and MemberPassword='{}'".format(em, pwd)
            cursor.execute(c)
            t = tuple(cursor.fetchall())
            if t == ():
                return render(request, 'error.html')
            else:
                return render(request, "memberpage.html")
        if request.POST.get("checkbox") == "employee":
            for key, value in d.items():
                if key == "email":
                    em = value
                if key == "password":
                    pwd = value
            c = "select * from employee where EmpID='{}' and EmpPassword='{}'".format(em, pwd)
            cursor.execute(c)
            t = tuple(cursor.fetchall())
            if t == ():
                return render(request, 'error.html')
            else:
                return render(request, "employeepage.html")

    return render(request, 'login.html')
def register(request):
    global fn, ln, em, pwd
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="1234", database='CarRenting')
        cursor = m.cursor()
        d = request.POST
        if request.POST.get("checkbox2")  == "employee":
            for key, value in d.items():
                if key == "first_name":
                    fn = value
                if key == "last_name":
                    ln = value
                if key == "email":
                    em = value
                if key == "password":
                    pwd = value

            c = "insert into employee Values('{}','{}')".format(em, pwd)
            cursor.execute(c)
            m.commit()
        if request.POST.get("checkbox2") == "member":
            for key, value in d.items():
                if key == "first_name":
                    fn = value
                if key == "last_name":
                    ln = value
                if key == "email":
                    em = value
                if key == "password":
                    pwd = value

            c = "insert into member Values('{}','{}')".format(em, pwd)
            cursor.execute(c)
            m.commit()
    return render(request,'register.html')

def book(request):
    global pickup, rent_id, model,returntime
    pickup = request.POST.get('datetime1')
    returntime = request.POST.get('datetime2')
    if request.POST.get('model') != None :
        model = request.POST.get('model')
        cars = Car_Selection.objects.filter(model__icontains = model)
        for e in cars:
            rent_id = e.vehicle_id
        return render(request,'book.html',{'cars':cars})
    return render(request,'search.html')


def info(request):
    global mname,mail,madd,mph,mbill,mcard,mdriv
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="1234", database='CarRenting')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "member name":
                mname = value
            if key == "member email":
                mail = value
            if key == "member address":
                madd = value
            if key == "member phone":
                mph = value
            if key == "billing":
                mbill = value
            if key == "card":
                mcard = value
            if key == "driving":
                mdriv = value
        x = "insert into membership_info Values('{}','{}')".format(mdriv,em)
        y = "insert into payment_info Values('{}','{}','{}')".format(mcard,mail,mbill)
        z = "insert into general_info Values('{}','{}','{}','{}','{}','{}','{}','{}')".format(mname,madd,mph,mail,pickup,returntime,model,rent_id)
        rent_history = Rental_History(model=model,memberID=em,vehicle_id=rent_id,pickup=pickup,returntime = returntime)
        rent_history.save()
        cursor.execute(x)
        cursor.execute(y)
        cursor.execute(z)
        m.commit()
    return render(request,'ginfo.html')
def history(request):
    history = Rental_History.objects.filter(memberID__icontains=em)
    return render(request, 'history.html', {'history': history})

def thank(request):
    return render(request,'thank.html')
def addcar(request):
    if request.method == 'POST':
        cmodel = request.POST.get('car model')
        id = request.POST.get('car id')
        color = request.POST.get('color')
        loc = request.POST.get('car loc')
        rate = request.POST.get('rate')
        capacity = request.POST.get('capacity')
        c  = Car_Selection(model = cmodel,color=color,vehicle_id=id,seating_capacity=capacity,rental_rate=rate,Location=loc)
        c.save()
    return render(request,'addcar.html')

def changeloc(request):
    veh = request.POST.get('car veh id')
    nloc = request.POST.get('car new loc')
    if request.POST.get('car new loc') != None:
        Car_Selection.objects.filter(vehicle_id=veh).update(Location = nloc)
    return render(request,'changeloc.html')