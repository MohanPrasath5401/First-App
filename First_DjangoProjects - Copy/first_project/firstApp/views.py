from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,Mark_attendance, MasterData
from .forms import Studentform,Studentform1, Masterform,MarkAttendance, OneStudentform
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import allowed_user

import time 


def about(request):
    return HttpResponse("<h1>Hello World</h1>")


def home(request):
    context = {'title': 'Project'}
    return render(request, 'firstApp/base.html', context)

posts = [{

    'roll_num': 20,
    'Name':"abc" ,
    'email' : "Abc@xyz.com"},

    {	'roll_num': 30,
    'Name':"nmb" ,
    'email' : "NMB@xyz.com"},   ]

def DataDisplay(request):
    context = {'data' : posts}
    return render(request, '/display_data.html', context )

def TableDisplay(request):
    posts = Student.objects.all()
    context = {'data' : posts}
    return render(request, '/table_display.html', context )

def StudentDisplay(request):
    form = Studentform()
    context = {'form': form}
    if request.method=='POST':
        form = Studentform(request.POST)
        try :
            print ("hello",form.is_valid())
            if form.is_valid():
                ID = form.cleaned_data.get('ID')
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                Class1 = form.cleaned_data['Class']
                Student.objects.create(stuid=ID,stuname=name,stumail=email,stuclass=Class1)
                messages.success(request,f"Record added for {name}")
                #return render(request,'firstApp/success.html', {'name':name})
            else:
                messages.warning(request,f"Error in the form")
        except Exception as e :
            print ("error",e)

    return render(request,'firstApp/display_student.html', context)

def Student_formModel(request):
    form = Studentform1()
    context = {'form': form}
    if request.method=='POST':
        form = Studentform1(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['stuname']
            messages.success(request,f"Record added {name}")
        else:
            messages.warning(request,f"Error in the form")
    return render(request,'firstApp/display_forms.html', context)

# Create your views here.
'''
@login_required(login_url='Login')
def master_Data(request):     # writeable 
    if request.user.groups.exists():
        if request.user.groups.all()[0].name=='grp_write':
            form = Masterform()
            context = {'form': form, 'legend': "Enter the Details "}
            if request.method=='POST':
                form = Masterform(request.POST)
                if form.is_valid():
                        try :
                        
                            form.save()
                            name = form.cleaned_data['stuname']
                            messages.success(request,f"Record added {name}")
                        except Exception as e :
                            messages.warning(request,f"{e}")
                else:
                    print (type(form.errors))
                    messages.warning(request,f"{form.errors}", )
            return render(request, 'firstApp/display_forms.html', context)
        else :
            return HttpResponse("<h1>You are not Authorized</h1>")
    else :
        return HttpResponse("<h1>You are not Authorized</h1>")
'''
@login_required(login_url='Login')
@allowed_user(allowed_roles=['grp_write'])
def master_Data(request):     # writeable 
            form = Masterform()
            context = {'form': form, 'legend': "Enter the Details "}

            if request.method=='POST':
                form = Masterform(request.POST)
                if form.is_valid():
                        try :
                        
                            form.save()
                            name = form.cleaned_data['stuname']
                            messages.success(request,f"Record added {name}")
                        except Exception as e :
                            messages.warning(request,f"{e}")
                else:
                    print (type(form.errors))
                    messages.warning(request,f"{form.errors}", )

            return render(request, 'firstApp/display_forms.html', context)

def e_h(t1):
    t9 = time.localtime(t1)
    return time.strftime("%d-%m-%Y-%H", t9)

def Mark_Attendance(request):
            form = MarkAttendance()
            context = {'form': form, 'legend': "Mark Your Attendance"}
            if request.method=='POST':
                form = MarkAttendance(request.POST)
                if form.is_valid():
                    mark1 = form.save(commit=False)
                    mark1.time1 = int(time.time())
                    mark1.ip_address = request.META.get('REMOTE_ADDR')
                    mark1.platform = request.META.get('HTTP_USER_AGENT')
                    mark1.date1 = e_h(mark1.time1)
                    form.save()
                    messages.success(request,f"Attendance Marked")
                    print ("OKKKK")


            return render(request,'firstApp/display_forms.html', context)
'''
def DisplayAttendance(request):
    if request.user.groups.exists():
        allowed_roles = ['grp1_read', 'grp_write']
        n_g = request.user.groups.all()[0].name
        if n_g in allowed_roles:
            posts = Mark_Attendance.objects.all()
            context = {'data' : posts}
            return render(request, 'firstApp/displayAtt.html', context )
        else :
            return HttpResponse("<h1>You are not Authorized</h1>")
    else :
        return HttpResponse("<h1>You are not Authorized</h1>")
'''
@allowed_user(allowed_roles=['grp_write','grp1_read'])
def DisplayAttendance(request):
            posts = Mark_Attendance.objects.all()
            context = {'data' : posts}
            return render(request, 'firstApp/displayAtt.html', context )


@login_required(login_url='Login')
def OneStudentForm(request):
    form = OneStudentform()
    context = {'form': form, 'legend': "Enter the UID"}

    if request.method=='POST':
        form = OneStudentform(request.POST)
        if form.is_valid():
            try :
                id1=  (form.cleaned_data.get('ID'))
                m1=MasterData.objects.filter(stuid=id1)[0]
                posts = Mark_Attendance.objects.filter(uid=m1)
                context = {'form': form, 'legend': "Enetr the UID",'data' : posts}
                
                return render(request, 'firstApp/oneAtt.html', context )
            except IndexError:
                messages.warning(request,f"UID is not valid")
            except Exception as e :
                messages.warning(request,f"{e}, {type(e)}")

    return render(request,'firstApp/oneAtt.html', context)


######################################################
# from here REST API

#####################################################

from .serializer import Att_serializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser

def Student_details(request,pk):
    try:
        stu = Student.objects.get(id=pk) #model complex object
        serializer = Att_serializer(stu)
        print("jjjjj",serializer.data)
        json_data = JSONRenderer().render(serializer.data)
        print("$$$$$",json_data)
    except Exception as e:
        print(e)
        json_data = {'Not get':"NIL"}
    return HttpResponse(json_data,content_type="application/json")

@csrf_exempt
def Student_api(request): #deserializer  #send data using 3rd party application
        #give name get url
    try:
        if request.method == "GET":
            json_data = request.body
            print("hello",json_data)         #this
            stream = io.BytesIO(json_data)   #is code to take data from API
            python_data = JSONParser().parse(stream)
            id1 = python_data.get('id')
            stu = Student.objects.get(id= id1)       #model complex object
            serializer = Att_serializer(stu)
            print("jjjjj",serializer.data)
            json_data = JSONRenderer().render(serializer.data)
            print("$$$$$",json_data)
    except Exception as e:
          print(e)
          json_data = {'Not get':"NIL"}       
    #return HttpResponse(json_data,content_type='application/json')


    if request.method =="POST":
            json_data = request.body
            print("hi", json_data)
            stream = io.BytesIO(json_data)         #this
            python_data = JSONParser().parse(stream)   #is code to take data from API
            serializer = Att_serializer(data=python_data)
            if serializer.is_valid():
                serializer.save()
                res = {'msg': "Data Created"} #giving response
                return JsonResponse(res,safe=False)
            json_data = JSONRenderer().render(serializer.errors) # if above condition if not valid
            return HttpResponse(json_data,content_type='application/json')
    

    if request.method =="PUT" :    #to update data
            json_data = request.body
            print("hi", json_data)
            stream = io.BytesIO(json_data)         #this
            python_data = JSONParser().parse(stream)   #is code to take data from API
            id1=python_data.get('stuid') #in myapp.py we r sending stuid # this comes from mysql
            stu = Student.objects.get(stuid=id1)
            serializer = Att_serializer(stu,data=python_data,partial=True)
            if serializer.is_valid():  
                serializer.save()
                res = {'msg': "Data Updated"}
                return JsonResponse(res,safe=False)
            json_data = JSONRenderer().render(serializer.errors) # if above condition if not valid
            return HttpResponse(json_data,content_type='application/json')


    if request.method =="DELETE" :    #to update data
            json_data = request.body
            print("hi", json_data,request)
            stream = io.BytesIO(json_data)         #this
            python_data = JSONParser().parse(stream)   #is code to take data from API
            id1=python_data.get('id') #in myapp.py we r sending stuid # this comes from mysql
            stu = Student.objects.get(id=id1) #model object
            stu.delete()
            res = {'msg': "Data deleted"}
            return JsonResponse(res,safe=False)
    
#########################

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])
def hello_world(request):
    if request.method == "GET":
        return Response({'msg':"This is a GET response"})
    
    if request.method == "POST":
        print ("hello", repr(request.data))
        #print("it", dir(request))
        return Response({'msg':"This is POST request"})

########### Class Based API ###################
from rest_framework.generics import ListAPIView

class StudentListAPI(ListAPIView):
     queryset = Student.objects.all() #filter or whatever u want to GET
     serializer_class = Att_serializer

from rest_framework.generics import RetrieveAPIView
class StudentRetrieveAPI(RetrieveAPIView):      
     queryset = Student.objects.all() 
     serializer_class = Att_serializer

from rest_framework.generics import CreateAPIView
class StudentCreateAPI(CreateAPIView):      
     queryset = Student.objects.all() 
     serializer_class = Att_serializer

from rest_framework.generics import UpdateAPIView
class StudentUpdateAPI(UpdateAPIView):      
     queryset = Student.objects.all() 
     serializer_class = Att_serializer

from rest_framework.generics import DestroyAPIView
class StudentDestroyAPI(DestroyAPIView):      
     queryset = Student.objects.all() 
     serializer_class = Att_serializer

from rest_framework.generics import RetrieveUpdateDestroyAPIView
class StudentRetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):      
     queryset = Student.objects.all() 
     serializer_class = Att_serializer

     

