from django.shortcuts import render
from .models import Register
from django.http import HttpResponse
from mysql.connector import Connect,Error

# Create your views here.
def register(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            r = Register(email=email,password=password)
            r.save()
            return render(request,"Question4/login.html")
        else:
            return render(request,'Question4/register.html')
    except Error as e:
        return HttpResponse(f"Error : {e}")
    
def login(request):
    try:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            r = Register.objects.get(email=email,password=password)
            return render(request,"Question4/menu.html")
        else:
            return render(request,'Question4/login.html')
    except Error as e:
        return HttpResponse(f"Error : {e}")
    
def connection():
    try:
        con = Connect(host="localhost",user="root",password="jadeja6",database='dbStudent')
        return con
    except Error as e:
        print(e)

def insertRec(request):
    try:
        con = connection()
        cursor = con.cursor()
        if request.method == 'GET':
            return render(request,'Question4/insert.html')
        else:
            rollno = int(request.POST.get('rollno'))
            name = request.POST.get('name')
            cmarks = int(request.POST.get('Cmarks'))
            cppmarks = int(request.POST.get('Cppmarks'))
            pymarks = int(request.POST.get('Pymarks'))
            cursor.callproc('Insert1',(rollno,name,cmarks,cppmarks,pymarks))
            con.commit()
            cursor.close()
            return HttpResponse("Record Inserted Successfully...")
    except Error as e:
        return HttpResponse(f"Error : {e}")
    
def deleteRec(request):
    con = connection()
    cursor = con.cursor()
    try:
        if request.method == 'GET':
            return render(request,'Question4/delete.html')
        else:
            name = request.POST.get('name')
            cursor.callproc('Delete1',(name,))
            con.commit()
            return HttpResponse("Record Deleted Successfully...")
    except Exception as e:
        return HttpResponse(f"Error : {e}")
    
def updateRec(request):
    con = connection()
    cursor = con.cursor()
    try:
        if request.method == 'GET':
            return render(request,'Question4/update.html')
        else:
            rollno = int(request.POST.get('rollno'))
            name = request.POST.get('name')
            cmarks = int(request.POST.get('Cmarks'))
            cppmarks = int(request.POST.get('Cppmarks'))
            pymarks = int(request.POST.get('Pymarks'))
            cursor.callproc('Update1',(rollno,name,cmarks,cppmarks,pymarks))
            con.commit()
            return HttpResponse("Record Updated Successfully...")
    except Exception as e:
        return HttpResponse(f"Error : {e}")

def selectRec(request):
    con = connection()
    cursor = con.cursor()
    try:
        mycontext = {}
        sql = "select * from tblstudent order by (cmarks + cppmarks + pythonmarks) desc limit 3"
        cursor.execute(sql)
        records = cursor.fetchall()
        recTotal = []
        for i in records:
            rollno, name, cmarks, cppmarks, pymarks = i
            total = cmarks + cppmarks + pymarks
            recTotal.append((rollno,name,cmarks,cppmarks,pymarks,total))
        mycontext['record'] = recTotal
        return render(request,'Question4/select.html',mycontext)
    except Exception as e:
        return HttpResponse(f"Error : {e}")