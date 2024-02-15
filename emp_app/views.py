from django.shortcuts import render,HttpResponse
from datetime import datetime
from .models import Employee,Role,Department
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request,'index.html')


def view_emp(request):
    emps=Employee.objects.all()
    context={
            'emps':emps
    }
    return render(request,'view_emp.html',context)


def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        role = int(request.POST['role'])
        dept = int(request.POST['dept'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        new_employee = Employee(first_name=first_name,
                                last_name=last_name,
                                salary=salary,
                                bonus=bonus,
                                phone=phone,
                                hire_date=datetime.now(),
                                role_id=role,
                                dept_id=dept)
        new_employee.save()
        return render(request,'index.html')
    elif request.method =='GET':
        return render(request,'add_emp.html')
    else:
        return HttpResponse("Failed")
   

    
def del_emp(request,emp_id = 0):
    if emp_id:
        try:
            emp_id_to_be_deleted=Employee.objects.get(id = emp_id)  #we use get here because employee_id is appearing in the url
            emp_id_to_be_deleted.delete()
            #return HttpResponse("Employee Has been removed Successfully")
            return render(request,"index.html")
        except:
            return HttpResponse("Enter a Valid Employee id")
    emps=Employee.objects.all()
   
    context={
        'emps':emps
    }
    return render(request,'del_emp.html',context)

def fil_emp(request):
    if request.method=='POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))
        if dept:
            emps = emps.filter(dept__name__icontains = dept)  #dept k baad we have used 2 underscores because name of department i the foreign key
        if role:
            emps= emps.filter(role__name__icontains=role)
        context={
            'emps':emps
        }
        return render(request,'view_emp.html',context)
    elif request.method=='GET':
        return render(request,'fil_emp.html')
    else:
        return HttpResponse("An Exception occured")
        

    return render(request,'fil_emp.html')