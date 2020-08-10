
from django.urls import path
from universite.views import *
from secondaryapp.views import  *
from contactapp.views import  *



urlpatterns = [

   path('secondary-categories', CategoryList.as_view(), name='CategoryList'),
   path('secondary-list/', SecondaryList.as_view(), name='SecondaryList'),
  path('secondary-detail/<str:name>',SecondaryDetail.as_view(),name='SecondaryDetail'),
   path('contactapp/subscribe/<str:name>', Subscribers.as_view(), name='subscribers'),
   path('contactapp/contacts/<str:name>',Contacts.as_view(), name='contacts'),
   path('universities/', UniversityLists.as_view()),
   path('universities/<int:pk>/', UniversityDetail.as_view(), name='detail'),
   path('programs/', ProgramList.as_view()),
   path('programs/<int:pk>/', ProgramDetail.as_view()),
   path('departments', DepartmentList.as_view()),
   path('Departments/<int:pk>/', DepartmentDetail.as_view()),
   path('Facults/',FacultLIst.as_view()),
   path('Facults/<int:pk>/',FacultDetail.as_view()),






]
