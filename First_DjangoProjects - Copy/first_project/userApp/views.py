from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages                        #because we create in hash form
from .forms import SignUP,UserUpdateForm,ProfileUpdateForm
from .models import Profile as MyProfile
from django.contrib.auth.models import User

# Create your views here.
def Profile(request):
    return render(request,"userApp/profile.html")

def Profile_user(request,id1):
    u1 = User.objects.filter(id=id1)[0]
    context = {'user1':u1}
    return render(request,"userApp/profile_user.html",context)

def loginpage(request):
    form = AuthenticationForm()
    context = {'form':form,"legend":'Login Now'}
    next = ""
    if request.GET:
        next = request.GET['next']
    if request.method == 'POST':
        form = AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                if next == "":
                   return redirect('profile')
                else:
                    return redirect(next)
            else:
                messages.warning(request,"username or password is incorrect")
    return render(request,"userApp/login.html",context)

def Register(request):
    form = SignUP()
    context = {'form':form,"legend":"Register Yourself Today"}
    if request.method == 'POST':
      form = SignUP(request.POST) 
      if form.is_valid():
        form.save()
        messages.success(request,f"Account Created")
        user1 = form.cleaned_data.get('username')
        user_obj = User.objects.filter(username=user1)[0]
        MyProfile.objects.create(user=user_obj)
        return redirect('Login')
    return render(request,"userApp/login.html",context)

def UpdateProfile(request):
        try:
            if request.method == 'POST' :
                u_form = UserUpdateForm(request.POST,instance=request.user)
                p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
                print("h1")
                if u_form.is_valid() and p_form.is_valid():
                    u_form.save()
                    p_form.save()
                    messages.success(request,"Profile Updated")
                    return redirect('profile')
            else:
                u_form = UserUpdateForm(request.POST,instance=request.user) 
                p_form = ProfileUpdateForm(request.POST,instance=request.user.profile)
                context = {'u_form':u_form,'p_form':p_form,"legend":"Update your Profile"}
                return render(request,"userApp/updateform.html",context)
        except User.RelatedObjectDoesNotExist:
            messages.info(request,"Profile Created Refresh Again")
            MyProfile.objects.create(user=request.user)
        except Exception as e :
            print(e,type(e))

def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = PasswordChangeForm(user=request.user,data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                messages.success(request,"Password changed successfully")
                return redirect('profile')
    
    fm = PasswordChangeForm(user=request.user)
    context = {'form':fm,'legend': "changed password"}
    return render(request,"userApp/login.html",context)














