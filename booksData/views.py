from django.shortcuts import render, HttpResponseRedirect
import booksData.forms as form
from django.contrib.auth.models import Group


# Create your views here.
def homePage(request):
    return render(request, 'base.html')

def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'adminClick.html')

def studentclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'studentClick.html')

def studentsignup_view(request):
    studentsignupform=form.StudentUserForm()
    if request.method=='POST':
        form1=form.StudentUserForm(request.POST)
        if studentsignupform.is_valid() :
            user=studentsignupform.save()
            user.set_password(user.password)
            user.save()
            my_student_group = Group.objects.get_or_create(name='STUDENT')
            my_student_group[0].user_set.add(user)

        return HttpResponseRedirect('studentlogin')
    return render(request,'studentSignUp.html',context={'form1': studentsignupform})

def adminsignup_view(request):
    adminsignupform=form.AdminSigupForm()
    if request.method=='POST':
        adminsignupform=form.AdminSigupForm(request.POST)
        if adminsignupform.is_valid():
            user=adminsignupform.save()
            user.set_password(user.password)
            user.save()
            my_admin_group = Group.objects.get_or_create(name='ADMIN')
            my_admin_group[0].user_set.add(user)

            return HttpResponseRedirect('adminlogin')
    return render(request,'adminSignUp.html',context={'form1': adminsignupform})

def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()

def afterlogin_view(request):
    if is_admin(request.user):
        print("after login Admin")
        return render(request,'adminAfterLogin.html')
    else:
        print("after login Student")
        return render(request,'studentAfterLogin.html')


# def adminlogin_view(request):
#     form1=form.Admin()
#     # if request.user.is_authenticated:
#     #     return HttpResponseRedirect('afterlogin')
#     return render(request,'adminSignUp.html',context={'form1': form1})
