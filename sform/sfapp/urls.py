from django.urls import path
from . import views

urlpatterns = [
    path('signin',views.inform1,name='inform'),
    path('',views.upform1,name='upform'),
    path('json',views.jj,name='upform'),
    path('cbv/',views.maya.as_view(),name='fdfd'),
    path('cbv/<slug:ff>',views.may,name='fdfd'),
    path('cruser',views.Newuser.as_view(),name='asdf')
]