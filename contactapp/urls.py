from django.urls import path,include
from contactapp import views

urlpatterns=[
  #  path('',views.Api.as_view(),name=views.Api.name),
    path('contactapp/subscribe/<str:name>',views.Subscribers.as_view(),name='subscribers'),
    path('contactapp/contacts/<str:name>',views.Contacts.as_view(),name='contacts'),

]