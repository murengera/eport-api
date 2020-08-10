from django.urls import path,include
from secondaryapp.views import *

urlpatterns=[
    #path('',views.ApiRoot.as_view(),name=views.ApiRoot.name),
    path('secondary-categories',CategoryList.as_view(),name='CategoryList'),
    path('category-detail/<str:name>',CategoryDetail.as_view(),name='CategoryDetail'),
    path('secondary-list',SecondaryList.as_view(),name='SecondaryList'),
    path('secondary-detail/<str:name>',SecondaryDetail.as_view(),name='SecondaryDetail'),
   

]