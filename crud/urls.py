
from django.urls import path
from .views import *

urlpatterns = [
    path('',add_show,name='addandshow'),
    path('delete/<int:id>/',delete_stud, name="deletedata"),
    path('update/<int:id>/',update_stud,name='updatedata'),
    
]
