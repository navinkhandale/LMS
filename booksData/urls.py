from django.urls import path

import booksData.views as vs
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', vs.homePage),
    path('adminclick', vs.adminclick_view),
    path('studentclick', vs.studentclick_view),
    path('adminlogin', LoginView.as_view(template_name='adminlogin.html')),
    path('studentlogin', LoginView.as_view(template_name='studentlogin.html')),
    path('adminsignup', vs.adminsignup_view),
    path('studentsignup', vs.studentsignup_view),
     path('logout', LogoutView.as_view(template_name='base.html')),
    path('afterlogin', vs.afterlogin_view),
   
]