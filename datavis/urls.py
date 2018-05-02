#from django.urls import path
from django.conf.urls import *
from . import views

urlpatterns = [
url('',views.index,name='index'),

]



"""
urlpatterns = [
    
    path('', views.index, name='index'),
]
"""
"""
urlpatterns=patterns('datavis.views',
    (r'^$', 'index'),
)"""